"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate

pip install exllamav2

pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

# https://github.com/Yukimura0119/EdgeAI_Final/blob/d41ad512c4f74af2e4b69e8177d6065bb4f718d9/result.py#L11
# https://github.com/zgce/exllamav2/blob/03b2d551b2a3a398807199456737859eb34c9f9c/doc/dynamic.md?plain=1#L164

from exllamav2.generator import ExLlamaV2DynamicGenerator

output = generator.generate(prompt = "Hello, my name is", max_new_tokens = 200)

outputs = generator.generate(
    prompt = [
        "Hello, my name is",
        "Once upon a time,",
        "Large language models are",
    ], 
    max_new_tokens = 200
)

