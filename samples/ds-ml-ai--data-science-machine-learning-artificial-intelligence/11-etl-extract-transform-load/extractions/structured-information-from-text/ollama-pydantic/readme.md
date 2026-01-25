

```python
from ollama import chat
from ollama import ChatResponse

class details(BaseModel):
    customer_name: str
    phone_number: str
    order_number: str
    addres: str

details_schema = details.model_json_schema()

prompt = """
Extract data from text:
{text}
"""

response: ChatResponse = chat(
                                model='gemma3:27b', 
                                messages=[
                                    {
                                        'role': 'user',
                                        'content': prompt,
                                    },
                                ], 
                                format = details_schema
                            )
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)

```

