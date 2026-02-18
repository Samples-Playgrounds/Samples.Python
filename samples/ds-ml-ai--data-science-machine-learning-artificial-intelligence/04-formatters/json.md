#

https://www.geeksforgeeks.org/python/convert-class-object-to-json-in-python/

https://www.geeksforgeeks.org/python/json-dumps-in-python/

https://docs.python.org/3/library/json.html

json

jsonpickle

# Source - https://stackoverflow.com/a
# Posted by minker
# Retrieved 2026-01-04, License - CC BY-SA 4.0

pip install objprint

# Source - https://stackoverflow.com/a
# Posted by minker
# Retrieved 2026-01-04, License - CC BY-SA 4.0

from objprint import objjson
t = testclass()
json_obj = objjson(t)
print(json.dumps(json_obj))

# Source - https://stackoverflow.com/a
# Posted by minker
# Retrieved 2026-01-04, License - CC BY-SA 4.0

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

# Source - https://stackoverflow.com/a
# Posted by Kurt Kline
# Retrieved 2026-01-04, License - CC BY-SA 4.0

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


# Source - https://stackoverflow.com/a
# Posted by Kurt Kline
# Retrieved 2026-01-04, License - CC BY-SA 4.0

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

