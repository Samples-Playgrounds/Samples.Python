
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

def model_init (model: str, request_timeout: int, context_window: int):
    global llm
    llm = Ollama(
        model=model,
        request_timeout=120.0,
        # Manually set the context window to limit memory usage
        context_window=8000,
    )


def model_prompt_response_chat_complete (prompt: str) -> str:

    resp = llm.complete(prompt)

    return resp


def model_role_prompt_response_chat_complete (role: str, prompt: str) -> str:
    messages = [
        ChatMessage(
            role=role,
            content=prompt
        ),
    ]

    resp = llm.chat(messages)

    return resp