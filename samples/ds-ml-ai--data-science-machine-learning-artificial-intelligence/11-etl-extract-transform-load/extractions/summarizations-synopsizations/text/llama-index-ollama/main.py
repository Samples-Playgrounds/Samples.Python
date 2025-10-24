"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install llama-index-llms-ollama
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""


import api_summarization_synopsization_llama_index_ollama as api

models=[
    "gemma3:12b",
    "gpt-oss:20b",
]
prompts1 = [
            "Explain the theory of relativity in simple terms.",
            "Who is Paul Graham?",
            "Tell me a joke."
        ]

from llama_index.core.llms import ChatMessage

prompts2 = [
            ChatMessage(
                role="system",
                content="You are a pirate with a colorful personality"
                ),
            ChatMessage(
                role="user",
                content="Explain the theory of relativity in simple terms."
            ),
            ChatMessage(
                role="user",
                content="Who is Paul Graham?"
            ),
            ChatMessage(
                role="user",
                content="Tell me a joke."
            )
        ]

for m in models:
    print("=" * 120)
    print(f"model={m}")
    api.model_init(model=m, request_timeout=120, context_window=32768)
    for p in prompts1:
        print("-" * 120)
        response = api.model_prompt_response_chat_complete(prompt=p)
        print(response)

for m in models:
    print("=" * 120)
    print(f"model={m}")
    api.model_init(model=m, request_timeout=120, context_window=32768)
    for p in prompts2:
        print("-" * 120)
        response = api.model_role_prompt_response_chat_complete(role=p.role, prompt=p.content)
        print(response)


# (
#         role="system", content="You are a pirate with a colorful personality"
#     ),
#     ChatMessage(role="user", content="What is your name"),
# ]

# llm = Ollama(model="gemma3:12b", request_timeout=360.0)
# response = llm.chat([ChatMessage("What's this? Provide a description without leading or trailing text.", additional_kwargs={"images": [ImageDocument(image_path=image_path)]})])

