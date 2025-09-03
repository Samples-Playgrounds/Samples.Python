# https://ollama.com/blog/openai-compatibility

"""
# ollama run gpt-oss:20b
ollama run llama3.3:latest

rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip3.13 install "openai"
pip3.13 freeze > requirements.txt
"""

from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

response = client.chat.completions.create(
  model="llama3.3:latest",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The LA Dodgers won in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

print(f"============================================================================")
print(response.choices[0].message.content)
print(f"============================================================================")
print(response)
