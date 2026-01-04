# semchunk

*   https://github.com/isaacus-dev/semchunk

*   https://github.com/makingkaiser/semchunk

*   https://github.com/BigBuildBench/umarbutler_semchunk

```shell
pip install semchunk
```

```python
import semchunk
import tiktoken                        # `transformers` and `tiktoken` are not required.
from transformers import AutoTokenizer # They're just here for demonstration purposes.

chunk_size = 4 # A low chunk size is used here for demonstration purposes. Keep in mind, `semchunk`
               # does not know how many special tokens, if any, your tokenizer adds to every input,
               # so you may want to deduct the number of special tokens added from your chunk size.
text = 'The quick brown fox jumps over the lazy dog.'

# You can construct a chunker with `semchunk.chunkerify()` by passing the name of an OpenAI model,
# OpenAI `tiktoken` encoding or Hugging Face model, or a custom tokenizer that has an `encode()`
# method (like a `tiktoken`, `transformers` or `tokenizers` tokenizer) or a custom token counting
# function that takes a text and returns the number of tokens in it.
chunker = semchunk.chunkerify('isaacus/kanon-tokenizer', chunk_size) or \
          semchunk.chunkerify('gpt-4', chunk_size) or \
          semchunk.chunkerify('cl100k_base', chunk_size) or \
          semchunk.chunkerify(AutoTokenizer.from_pretrained('isaacus/kanon-tokenizer'), chunk_size) or \
          semchunk.chunkerify(tiktoken.encoding_for_model('gpt-4'), chunk_size) or \
          semchunk.chunkerify(lambda text: len(text.split()), chunk_size)

# If you give the resulting chunker a single text, it'll return a list of chunks. If you give it a
# list of texts, it'll return a list of lists of chunks.
assert chunker(text) == ['The quick brown fox', 'jumps over the', 'lazy dog.']
assert chunker([text], progress = True) == [['The quick brown fox', 'jumps over the', 'lazy dog.']]

# If you have a lot of texts and you want to speed things up, you can enable multiprocessing by
# setting `processes` to a number greater than 1.
assert chunker([text], processes = 2) == [['The quick brown fox', 'jumps over the', 'lazy dog.']]

# You can also pass an `offsets` argument to return the offsets of chunks, as well as an `overlap`
# argument to overlap chunks by a ratio (if < 1) or an absolute number of tokens (if >= 1).
chunks, offsets = chunker(text, offsets = True, overlap = 0.5)
```