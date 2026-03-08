#

https://www.geeksforgeeks.org/python/convert-class-object-to-json-in-python/

https://www.geeksforgeeks.org/python/json-dumps-in-python/

https://docs.python.org/3/library/json.html

json 

    https://docs.python.org/3/library/json.html

Orjson










Fastest JSON Libraries:
1. Orjson (Fastest - Recommended)
- 5-10x faster than json
- Uses Rust under the hood
- Same API as json with minor differences
2. ujson (UltraJSON)
- 2-5x faster than json
- Well-established alternative
3. RapidJSON (via pyrapidjson)
- Very fast C++ implementation
- Good performance
4.simdjson (via pysimdjson)
- Uses SIMD instructions
- Excellent for large JSON
Quick Comparison for Your Use Case:
For the performance timing data in docling (small dicts ~200-500 bytes):
| Library | Speed vs json | Memory | Notes |
|---------|--------------|--------|-------|
| orjson | 5-10x faster | Similar | Best overall, but returns bytes |
| ujson | 2-3x faster | Similar | Drop-in replacement |
| rapidjson | 3-5x faster | Similar | Good C++ impl |
| simdjson | 3-6x faster | Higher | Best for large files |
Recommendation for This Codebase:
Use orjson - install with pip install orjson
Replace:
import json
json.dumps(data, indent=4)
With:
import orjson
orjson.dumps(data, option=orjson.OPT_INDENT_2).decode()
Or for maximum performance (no indentation):
orjson.dumps(data)
The performance gain would be most noticeable when:
- Processing many documents
- Writing large performance data files
- Running benchmarks with many iterations

jsonpickle

pip install objprint


from objprint import objjson
t = testclass()
json_obj = objjson(t)
print(json.dumps(json_obj))


from objprint import op
t = testclass()
op(t, format="json", indent=2)

# If you want to dump to a file
with open("my_obj.json", "w") as f:
    # This is the same usage as print
    op(t, format="json", file=f)

Jsonic

https://github.com/OrrBin/Jsonic

pip install py-jsonic

from jsonic import serialize, deserialize
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    name: str
    email: str
    created_at: datetime

user = User("Alice", "alice@example.com", datetime.now())
json_data = serialize(user)  # Dict or JSON string
user_copy = deserialize(json_data, expected_type=User)  # Type-safe!




https://docs.pydantic.dev/latest/


from pydantic import BaseModel

class testclass(BaseModel):
    value1: str = "a"
    value2: str = "b"

test = testclass()

>>> print(test.json(indent=4))
{
    "value1": "a",
    "value2": "b"
}


import json
from pydantic.dataclasses import dataclass
from pydantic.json import pydantic_encoder

@dataclass
class testclass:
    value1: str = "a"
    value2: str = "b"

test = testclass()
>>> print(json.dumps(test, indent=4, default=pydantic_encoder))
{
    "value1": "a",
    "value2": "b"
}

