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


    for source_file in files_private_strives_ai_pdf_tests:
        print(120 * "=")
        print(f"source: {source_file}")
        for (library_name, file_name) in libs_extraction_text_from_documents_pdf:
            file = f"{source_file}.hwaifs/extractions/text/py/{library_name}/{file_name}"
            if not os.path.isfile(file):
                print(f"    file not found: {file}")
                continue

            with open(file, "r") as f:
                text = f.read()

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




