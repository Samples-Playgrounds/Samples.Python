"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

pip install deepagents
pip install tavily-python
pip install httpx
pip install markdownify
pip install langchain-core
pip install langchain-anthropic
pip install langchain-ollama
pip install stringcase

pip install orjson
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""


topics = \
    [
        "research context engineering approaches used to build AI agents",
        "research .NET agent frameworks and libraries",
    ]

from research import research_topics

research_topics(topics)




