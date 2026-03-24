# iree

```shell
pip install iree-tokenizer
```


```python
from iree.tokenizer import Tokenizer

tok = Tokenizer.from_file("tokenizer.json")

# Or load a tiktoken vocabulary
tok = Tokenizer.from_tiktoken("cl100k_base.tiktoken", encoding="cl100k_base")

# Encode / decode
ids = tok.encode("Hello world")          # [15496, 995]
text = tok.decode(ids)                    # "Hello world"

# Batch
tok.encode_batch(["Hello", "world"])      # [[15496], [995]]

# Numpy (zero-copy)
arr = tok.encode_to_array("Hello world")  # int32 ndarray

# Rich encoding with byte offsets
enc = tok.encode_rich("Hello world", track_offsets=True)
# enc.ids, enc.offsets, enc.type_ids

# Streaming decode (LLM token-at-a-time pattern)
from iree.tokenizer import decode_stream_iter
for chunk in decode_stream_iter(tok, token_generator):
    print(chunk, end="", flush=True)
```