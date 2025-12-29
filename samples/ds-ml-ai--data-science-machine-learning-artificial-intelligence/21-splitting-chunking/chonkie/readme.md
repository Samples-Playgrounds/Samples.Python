# `chonkie`

*   https://github.com/chonkie-inc/chonkie

*   https://docs.chonkie.ai/common/welcome

```shell
pip install "chonkie[all]"
```

Basic:

```python
# First import the chunker you want from Chonkie
from chonkie import RecursiveChunker

# Initialize the chunker
chunker = RecursiveChunker()

# Chunk some text
chunks = chunker("Chonkie is the goodest boi! My favorite chunking hippo hehe.")

# Access chunks
for chunk in chunks:
    print(f"Chunk: {chunk.text}")
    print(f"Tokens: {chunk.token_count}")

```

Pipeline:

```python
from chonkie import Pipeline

# Create a pipeline with multiple chunking and refinement steps
pipe = (
    Pipeline()
    .chunk_with("recursive", tokenizer="gpt2", chunk_size=2048, recipe="markdown")
    .chunk_with("semantic", chunk_size=512)
    .refine_with("overlap", context_size=128)
    .refine_with("embeddings", embedding_model="sentence-transformers/all-MiniLM-L6-v2")
)

# CHONK some Texts!
doc = pipe.run(texts="Chonkie is the goodest boi! My favorite chunking hippo hehe.")

# Access the processed chunks in the `doc` object
for chunk in doc.chunks:
    print(chunk.text)
```


```python

```