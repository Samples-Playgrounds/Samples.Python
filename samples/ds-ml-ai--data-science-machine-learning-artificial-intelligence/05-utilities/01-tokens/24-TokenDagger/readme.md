# TokenDagger

*   https://github.com/M4THYOU/TokenDagger

*   https://news.ycombinator.com/item?id=44422480

```shell
pip install tokendagger
```

```python
# import tiktoken --- Remove this line!
import tokendagger as tiktoken

# ...

tokenizer = tiktoken.Encoding(
    name=name,
    pat_str=pattern,
    mergeable_ranks=vocab,
    special_tokens=special_tokens,
)
```