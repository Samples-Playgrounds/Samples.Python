# Tokens

* OpenAI Price: Calculate Tokens with Python

  * https://www.youtube.com/watch?v=Iu2WC7uaSWY

    * https://github.com/openai/tiktoken

```
import tiktoken
enc = tiktoken.get_encoding("o200k_base")
assert enc.decode(enc.encode("hello world")) == "hello world"

# To get the tokeniser corresponding to a specific model in the OpenAI API:
enc = tiktoken.encoding_for_model("gpt-4o")

encoding = tiktoken.encoding_for_model('gpt-4o-mini')

```

Tokenizer libraries by language

For o200k_base, cl100k_base and p50k_base encodings:

  Python: tiktoken
  
  .NET / C#: 

    SharpToken,

    TiktokenSharp

For r50k_base (gpt2) encodings, tokenizers are available in many languages.

  Python: 

    tiktoken (or alternatively GPT2TokenizerFast)

  .NET / C#: 

    GPT Tokenizer

https://developers.openai.com/cookbook/examples/how_to_count_tokens_with_tiktoken/

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


o200k_base: 
cl100k_base: 
p50k_base: 
r50k_base:
