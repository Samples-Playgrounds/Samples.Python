# Tokens

*   tiktoken

*   hugging face

*   iree

    *   https://github.com/iree-org/iree-tokenizer-py


* OpenAI Price: Calculate Tokens with Python

  * https://www.youtube.com/watch?v=Iu2WC7uaSWY

    * https://github.com/openai/tiktoken

```python
import tiktoken
enc = tiktoken.get_encoding("o200k_base")
assert enc.decode(enc.encode("hello world")) == "hello world"

# To get the tokeniser corresponding to a specific model in the OpenAI API:
enc = tiktoken.encoding_for_model("gpt-4o")

encoding = tiktoken.encoding_for_model('gpt-4o-mini')

```

## Tokenizer libraries by language

For o200k_base, cl100k_base and p50k_base encodings:

    *   Python
  
        *   tiktoken
  
    *   .NET / C#: 

        *   SharpToken

            *   https://github.com/dmitry-brazhenko/SharpToken

    *   TiktokenSharp

        *   https://github.com/aiqinxuancai/TiktokenSharp


For r50k_base (gpt2) encodings, tokenizers are available in many languages.

    *   Python: 

        *   tiktoken (or alternatively GPT2TokenizerFast)

    *   .NET / C#: 

        *   GPT Tokenizer

*   https://developers.openai.com/cookbook/examples/how_to_count_tokens_with_tiktoken/

*   `Microsoft.ML.Tokenizers`

    *   https://www.nuget.org/packages/Microsoft.ML.Tokenizers

```python
import tiktoken

encoding = tiktoken.get_encoding(
                                    # Encoding for the newest GPT-4o-Mini model.
                                    "o200k_base"
                                    # Encoding model for newer OpenAI models such as GPT-4 and GPT-3.5-Turbo.
                                    # "cl100k_base"
                                    # Encoding for Codex models, these models are used for code applications.
                                    # "p50k_base"
                                    # Older encoding for different versions of GPT-3.
                                    # "r50k_base"
                                )
encoding = tiktoken.encoding_for_model(
                                        "gpt-4o-mini"
                                        ) 
prompt = "tiktoken is great!"
encoding_array = encoding.encode(prompt)
```

*   https://www.datacamp.com/de/tutorial/tiktoken-library-python

*   https://www.datacamp.com/tutorial/estimating-cost-of-gpt-using-tiktoken-library-python

*   https://stackoverflow.com/questions/76106366/how-to-use-tiktoken-in-offline-mode-computer

*   https://medium.com/@ilyesrezgui46/enhance-your-gpt-experience-tiktoken-unveiled-free-token-counting-for-prompts-with-python-code-51851883825b

*   https://github.com/felvin-search/token-count

*   https://github.com/felvin-search/token-count/blob/master/token_count/token_count.py

```
Rules of Thumb (English):
1 token       4 characters.
1 token       0.75 words.
100 tokens    75 words.
```

*   https://dev.to/aairom/counting-the-number-of-tokens-sent-to-a-llm-in-go-part-1-3coo

*   https://console.upstage.ai/docs/guides/counting-tokens

```python
from tokenizers import Tokenizer
 
# Check out the tokenizers listed below.
# If you're using Solar Mini or Embeddings model, make sure to use "upstage/solar-1-mini-tokenizer".
tokenizer = Tokenizer.from_pretrained("upstage/solar-pro2-tokenizer")
 
text = "Hi, how are you?"
enc = tokenizer.encode(text)
print("Encoded input:")
print(enc)
 
inv_vocab = {v: k for k, v in tokenizer.get_vocab().items()}
tokens = [inv_vocab[token_id] for token_id in enc.ids]
print("Tokens:")
print(tokens)
 
number_of_tokens = len(enc.ids)
print("Number of tokens:", number_of_tokens)
 
# Truncate tokens
token_length_limit = 4000
truncated_text = tokenizer.decode(enc.ids[:4000])
print("Truncated text: ")
print(truncated_text)
```

*   https://ai.google.dev/gemini-api/docs/tokens

```python
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
                                            model="gemini-3-flash-preview", 
                                            contents=prompt
                                        )
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
                                            model="gemini-3-flash-preview", 
                                            contents=prompt
)

print(response.usage_metadata)
```



*   https://github.com/tropptr-torrptrop/token-counter

```shell
pip install tiktoken transformers anthropic
```

*   https://github.com/tropptr-torrptrop/token-counter/blob/main/token_counter.pyw

*   https://github.com/sammcj/ingest


*   https://www.dsdev.in/counting-tokens-at-scale-using-tiktoken

```python
text = "Large string ....."
token_count = len(text) // 4
```

```python
text = "Large string ....."
token_count = model.encode_to_numpy(text).shape[0]
```


*   https://www.prompttokencounter.com/

*   https://token-count.streamlit.app/

*   https://gptforwork.com/tools/tokenizer

*   https://platform.openai.com/tokenizer

*   https://medium.com/google-cloud/counting-gemini-text-tokens-locally-with-the-vertex-ai-sdk-78979fea6244

*   https://promptprep.readthedocs.io/en/stable/token_counting.html


```csharp
var punctuation = text.Where(Char.IsPunctuation).Distinct().ToArray();
var words = text.Split().Select(x => x.Trim(punctuation));


var fixedInput = Regex.Replace(input, "[^a-zA-Z0-9% ._]", string.Empty);
// This regex doesn't support apostrophe so the extension method is better
```


*   https://stackoverflow.com/questions/16725848/how-to-split-text-into-words


*   https://stackoverflow.com/questions/743806/how-do-i-split-a-string-into-a-list-of-words
    

```python
words = text.split()      

words = text.split(",")   
```

```python
import nltk
words = nltk.word_tokenize(raw_sentence)
```


```python
text.split()
```


```python
import string
[word.strip(string.punctuation) for word in text.split()]
```



```python
import shlex
shlex.split("sudo echo 'foo && bar'")
```



```python
print(list("word"))
#  ['w', 'o', 'r', 'd']
```

```python
print(list("some sentence"))
#  ['s', 'o', 'm', 'e', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e']
```