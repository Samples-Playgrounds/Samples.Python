"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate

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
            "This is an example sentence, showing off the tokenization process.",
            """
            In the face of changing market conditions and pressure to accelerate growth, the ability for customers to
            do more with less is critical. And while the cloud has long been the north star for realizing efficiencies
            and accelerating innovation, at Microsoft, we understand that these benefits also need to happen outside
            of the cloud. In 2021 we announced the general availability of Azure Arc-enabled SQL Managed Instance.
            Previously only available in Azure, Azure Arc-enabled SQL Managed Instance allows customers to build new
            cloud native applications on any infrastructure, in their on-premises environments and across other public
            clouds. Now, we are offering a way for customers to make the most of their legacy applications, with Azure
            Arc-enabled SQL Server.
            """,
        ]

for text in texts:
    print(120 * "=")
    words = text.split()      
    print(words)
    print(100 * ".")
    words = text.split(",")   
    print(words)
    print(100 * ".")
    print(list(text))
    print(100 * ".")
    count_characters = len(text) // 4
    print(f"count characters: {count_characters}")
    count_tokens = count_characters // 4
    print(f"count tokens: {count_tokens}")

import api_tokens_stdlib_split as api

import sys
import os
scriptpath = "../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *


def main():

    for text in texts:
        print(120 * "=")
        result_1 = api.tokens_characters_in_text(text)
        print(f"characters: {result_1[0]}")
        print(f"         count characters   : {result_1[1]}")
        print(f"         count tokens       : {result_1[2]}")
        result_2 = api.tokens_words_in_text(text)
        print(f"words: {result_2[0]}")
        print(f"         count words        : {result_2[1]}")
        print(f"         count tokens min   : {result_2[2]}")
        print(f"         count tokens max   : {result_2[3]}")

   

if __name__ == '__main__':
    main()






