"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python3.14 -m venv .venv
source .venv/bin/activate
pip3.14 install --upgrade pip

pip3.14 install "smolagents"
pip3.14 install "smolagents[toolkit]"
pip3.14 install OpenAi

pip3.14 install orjson
pip3.14 install timer
pip3.14 install codetiming
pip3.14 freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import os


from smolagents import CodeAgent, WebSearchTool, InferenceClientModel
from smolagents import OpenAIModel

# model = InferenceClientModel()

model = OpenAIModel(
                        model_id="Qwen3.6-35B-A3B",
                        api_base="http://127.0.0.1:11454/v1",
                        # os.environ["OPENAI_API_KEY"],
                        api_key="local",
                    )
#                        temperature=0.7,
#                        max_tokens=255000,
#                        top_p=0.9

agent = CodeAgent(
                        tools=[
                                WebSearchTool()
                                ],
                        model=model,
                        stream_outputs=True
                )
agent.run(
            """
            How many seconds would it take for a leopard at full speed to run through Pont des Arts?
            """
        )
