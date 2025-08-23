
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

def model_init (model: str, request_timeout: int, context_window: int):
    global llm
    llm = Ollama(
        model="gemma3:12b",
        request_timeout=120.0,
        # Manually set the context window to limit memory usage
        context_window=8000,
    )


def model_complete (prompt: str) -> str:
    llm = Ollama(
        model="gemma3:12b",
        request_timeout=120.0,
        # Manually set the context window to limit memory usage
        context_window=8000,
    )

    resp = llm.complete(prompt)

    return resp


def model_chat (role: str, prompt: str) -> str:
    messages = [
        ChatMessage(
            role=role, content=prompt
        ),
    ]

    resp = llm.chat(messages)

    return resp