
https://docs.perplexity.ai/docs/search/quickstart


```shell
export PERPLEXITY_API_KEY="your_api_key_here"
pip install perplexityai
```

```python
from perplexity import Perplexity

client = Perplexity()

search = client.search.create(
    query="latest AI developments 2024",
    max_results=5,
    max_tokens_per_page=4096
)

for result in search.results:
    print(f"{result.title}: {result.url}")

```


```shell
curl -X POST 'https://api.perplexity.ai/search' \
  -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "latest AI developments 2024",
    "max_results": 5,
    "max_tokens_per_page": 4096
  }' \
  | \
  jq
  ```