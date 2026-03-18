"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install tiktoken
pip install orjson
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

texts = [
            """
            """,
            "",
            "Large string .....",
            "word",
            "some sentence",
            "tiktoken is great!",
        ]


import api_tokens_tiktoken as api

import sys
import os
scriptpath = "../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *


def main():

    for text in texts:
        print(120 * "=")
        result_1 = api.tokens_in_text_for_encoding(text, "o200k_base")
        print(f"tokens          : {result_1[0]}")
        print(f"tokens decoded  : {result_1[2]}")
        print(f"         count tokens       : {result_1[1]}")
        result_1 = api.tokens_in_text_for_encoding(text, "cl100k_base")
        print(f"tokens          : {result_1[0]}")
        print(f"tokens decoded  : {result_1[2]}")
        print(f"         count tokens       : {result_1[1]}")

        print(120 * "-")
        result_2 = api.tokens_in_text_for_model(text, "gpt-4o")
        print(f"tokens          : {result_2[0]}")
        print(f"tokens decoded  : {result_2[2]}")
        print(f"         count tokens       : {result_2[1]}")
        result_2 = api.tokens_in_text_for_model(text, "text-embedding-ada-002")
        print(f"tokens          : {result_2[0]}")
        print(f"tokens decoded  : {result_2[2]}")
        print(f"         count tokens       : {result_2[1]}")
   

if __name__ == '__main__':
    main()

