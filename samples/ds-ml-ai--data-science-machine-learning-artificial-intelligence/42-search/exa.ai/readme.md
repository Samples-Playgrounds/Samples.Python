Exa

Exa.ai 

    https://exa.ai/pricing

https://exa.ai/search

```python
from exa_py import Exa
exa = Exa(api_key = "EXA-API-KEY")
result = exa.search(
  "Tko ima teret dokazivanja u kaznenom postupku za klevetu u Hrvatskoj?",
  type = "instant"
)
```

```shell
curl \
  -X POST https://api.exa.ai/search \
  -H "x-api-key: EXA-API-KEY" \
  -H "Content-Type: application/json" \
  -d '
  {
    "query": "Tko ima teret dokazivanja u kaznenom postupku za klevetu u Hrvatskoj?",
    "type": "instant"
  }
  '
```