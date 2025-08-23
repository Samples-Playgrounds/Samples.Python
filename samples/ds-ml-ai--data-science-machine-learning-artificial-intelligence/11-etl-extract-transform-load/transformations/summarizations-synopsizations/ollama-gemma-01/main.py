# not a comment, string literal used as a docstring
"""
python -m venv .venv
source .venv/bin/activate
pip install llama-index-llms-ollama
pip freeze > requirements.txt
"""

import api_llama_index_ollama as api

api.model_init(model="gemma3:12b", request_timeout=120, context_window=8000)

print("-" * 120)
prompt="Explain the theory of relativity in simple terms."
response = api.model_complete(prompt=prompt)
print(response)

print("-" * 120)
prompt="Who is Paul Graham?"
response = api.model_complete(prompt=prompt)
print(response)

print("-" * 120)
prompt="Tell me a joke."
response = api.model_complete(prompt)
print(response)


api.model_init(model="gpt-oss:20b", request_timeout=120, context_window=8000)

print("-" * 120)
prompt="Explain the theory of relativity in simple terms."
response = api.model_complete(prompt=prompt)
print(response)

print("-" * 120)
prompt="Who is Paul Graham?"
response = api.model_complete(prompt=prompt)
print(response)

print("-" * 120)
prompt="Tell me a joke."
response = api.model_complete(prompt)
print(response)


# (
#         role="system", content="You are a pirate with a colorful personality"
#     ),
#     ChatMessage(role="user", content="What is your name"),
# ]

# llm = Ollama(model="gemma3:12b", request_timeout=360.0)
# response = llm.chat([ChatMessage("What's this? Provide a description without leading or trailing text.", additional_kwargs={"images": [ImageDocument(image_path=image_path)]})])

