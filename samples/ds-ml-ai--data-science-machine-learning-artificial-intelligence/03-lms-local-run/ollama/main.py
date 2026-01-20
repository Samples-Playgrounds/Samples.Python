"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate

pip install ollama

pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

"""
"""

models = [
        "qwen3-coder:30b",
        "codegeex4:9b",
        "codebooga:34b",
        "codeup:13b",
        "cogito:70b",
        "codeqwen:7b",
        "cogito:32b",
        "codegemma:7b",
        "codellama:34b",
        "codellama:70b",
        "codellama:13b",
        "devstral-small-2:latest",
        "devstral-2:latest",
        "karanchopda333/whisper:latest",
        "all-minilm:latest",
        "qwen3-coder:latest",
        "ibm/granite3.3:8b",
        "granite-code:34b",
        "granite4:3b",
        "wizardcoder:33b",
        "granite3.3:8b",
        "llava:34b",
        "gemma3:4b",
        "gemma3:27b",
        "gemma3:latest",
        "gemma3:12b",
        "gpt-oss:120b",
        "gpt-oss:20b",
        "gpt-oss:latest",
        "phind-codellama:34b",
        "mistral-large:latest",
        "phind-codellama:latest",
        "codegemma:latest",
        "mistral-large:123b",
        "deepseek-coder-v2:236b",
        "deepseek-coder-v2:latest",
        "deepseek-coder:latest",
        "llama3.3:latest",
        "deepseek-coder:33b",
        "qwq:latest",
        "marco-o1:latest",
        "phi4:latest",
        "deepseek-r1:latest",
        "nomic-embed-text:latest",
        "phi3.5:latest",
        "phi:latest",
        "llama3.2-vision:latest",
]

from ollama import chat
from ollama import ChatResponse


def main():
    for model in models:
        print("=" * 120)
        print(f"model <- models = {model}")

        response = chat(model=model, messages=[
            {
                'role': 'user',
                'content': 
                """
                List your technical capabilities. Specifically, tell me:
                Your maximum context window (in tokens).
                Do you support native video input (e.g., MP4) or just keyframe analysis?
                What is your training data cutoff?
                Can you process audio files directly?
                What image file formats do you support?
                """,
            },
        ])
        print(response['message']['content'])
        # or access fields directly from the response object
        print(response.message.content)

if __name__ == "__main__":
    main()
