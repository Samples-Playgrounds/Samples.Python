# Readme

readme.md

*   https://github.com/speedyk-005/chunklet

*   https://speedyk-005.github.io/chunklet-py/latest/


```python
from chunklet.sentence_splitter import SentenceSplitter

TEXT = """
She loves cooking. He studies AI. "You are a Dr.", she said. The weather is great. We play chess. Books are fun, aren't they?

The Playlist contains:
  - two videos
  - one image
  - one music

Robots are learning. It's raining. Let's code. Mars is red. Sr. sleep is rare. Consider item 1. This is a test. The year is 2025. This is a good year since N.A.S.A. reached 123.4 light year more.
"""

splitter = SentenceSplitter(verbose=True)
sentences = splitter.split(TEXT, lang="en")

for sentence in sentences:
    print(sentence)
```


```python
from chunklet.sentence_splitter import SentenceSplitter

lang_texts = {
    "en": "This is a sentence. This is another sentence. Mr. Smith went to Washington. He said 'Hello World!'. The quick brown fox jumps over the lazy dog.",
    "fr": "Ceci est une phrase. Voici une autre phrase. M. Smith est allé à Washington. Il a dit 'Bonjour le monde!'. Le renard brun et rapide saute par-dessus le chien paresseux.",
    "es": "Esta es una oración. Aquí hay otra oración. El Sr. Smith fue a Washington. Dijo '¡Hola Mundo!'. El rápido zorro marrón salta sobre el perro perezoso.",
    "de": "Dies ist ein Satz. Hier ist ein weiterer Satz. Herr Smith ging nach Washington. Er sagte 'Hallo Welt!'. Der schnelle braune Fuchs springt über den faulen Hund.",
    "hi": "यह एक वाक्य है। यह एक और वाक्य है। श्री स्मिथ वाशिंगटन गए। उसने कहा 'नमस्ते दुनिया!'। तेज भूरा लोमड़ी आलसी कुत्ते पर कूदता है।"
}

splitter = SentenceSplitter()

for lang, text in lang_texts.items():
    detected_lang, confidence = splitter.detected_top_language(text)
    print(f"Original language: {lang}")
    print(f"Detected language: {detected_lang} with confidence {confidence:.2f}")
    print("-" * 20)

```



```python
import re
from chunklet.sentence_splitter import SentenceSplitter, CustomSplitterRegistry


splitter = SentenceSplitter(verbose=False)
registry = CustomSplitterRegistry()

@registry.register("en", name="MyCustomEnglishSplitter")
def my_custom_splitter(text: str) -> list[str]:
    """A simple custom sentence splitter"""
    return [s.strip() for s in re.split(r'(?<=\\.)\s+', text) if s.strip()]

text = "This is the first sentence. This is the second sentence. And the third."
sentences = splitter.split(text=text, lang="en")

print("---" + " Sentences using Custom Splitter ---")
for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")

# Example with a custom splitter for multiple languages
@registry.register("fr", "es", name="MultiLangExclamationSplitter")
def multi_lang_splitter(text: str) -> list[str]:
    return [s.strip() for s in re.split(r'(?<=!)\s+', text) if s.strip()]

splitter_multi = SentenceSplitter(verbose=False)

text_fr = "Bonjour! Comment ça va? C'est super. Au revoir!"
sentences_fr = splitter_multi.split(text=text_fr, lang="fr")
print("\n--- Sentences using Multi-language Custom Splitter (French) ---")
for i, sentence in enumerate(sentences_fr):
    print(f"Sentence {i+1}: {sentence}")

text_es = "Hola. Qué tal? Muy bien! Adiós."
sentences_es = splitter_multi.split(text=text_es, lang="es")
print("\n--- Sentences using Multi-language Custom Splitter (Spanish) ---")
for i, sentence in enumerate(sentences_es):
    print(f"Sentence {i+1}: {sentence}")


# Unregistering Custom Splitters
registry.unregister("en")
```


```python
text = """
# Introduction to Chunking

This is the first paragraph of our document. It discusses the importance of text segmentation for various NLP tasks, such as RAG systems and summarization. We aim to break down large documents into manageable, context-rich pieces.

## Why is Chunking Important?

Effective chunking helps in maintaining the semantic coherence of information. It ensures that each piece of text retains enough context to be meaningful on its own, which is crucial for downstream applications.

### Different Strategies

There are several strategies for chunking, including splitting by sentences, by a fixed number of tokens, or by structural elements like headings. Each method has its own advantages depending on the specific use case.

---

## Advanced Chunking Techniques

Beyond basic splitting, advanced techniques involve understanding the document's structure. For instance, preserving section breaks can significantly improve the quality of chunks for hierarchical documents. This section will delve into such methods.

### Overlap Considerations

To ensure smooth transitions between chunks, an overlap mechanism is often employed. This means that a portion of the previous chunk is included in the beginning of the next, providing continuity.

---

# Conclusion

In conclusion, mastering chunking is key to unlocking the full potential of your text data. Experiment with different constraints to find the optimal strategy for your needs.
"""
```


```python
from chunklet.plain_text_chunker import PlainTextChunker

chunker = PlainTextChunker()  

chunks = chunker.chunk(
    text=text,
    lang="auto",             
    max_sentences=2,
    overlap_percent=0,       
    offset=0                 
)

for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(f"Metadata: {chunk.metadata}")
    print(f"Content: {chunk.content}")
    print()
```


```python
from chunklet.plain_text_chunker import PlainTextChunker

# Simple counter for demonstration purpose
def word_counter(text: str) -> int:
    return len(text.split())

chunker = PlainTextChunker(token_counter=word_counter)
```


```python
chunks = chunker.chunk(
    text=text,
    lang="auto",
    max_tokens=12,
)

for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(f"Content: {chunk.content}")
    print()
```