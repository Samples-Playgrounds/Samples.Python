"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install deep-translator
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_translate_deep_translator as api

import sys
import os
scriptpath = "../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *

root="../../../../../../data/"
# only smaller documents for testing
sources = files_documents_pdfs_cheat_sheets

translators = [
   "google",
   "pons",
   "mymemory",
   "yandex",
   "chatgpt",
   "linguee",
   "papago",
   # API key needed
   # MSFT_ENV_VAR
   "microsoft",
   # API key needed
   "deepl",
   # API key needed
   "qcri"
]

def main():

   for source in sources:
      print (120*"=")
      print(f"deep-translate <- source = {source}")
      for lib in libs_extraction_from_documents_pdf:
         print (80*"-")
         print(f"   using lib = {lib}")

         for translator in translators:
            print(f"      using translator = {translator}") 

            file = f"{source}.hwaifs/text/py/{lib}/content.txt"
            if os.path.exists(file):
               print(f"       Translating file = {file}")
               result_txt = api.translate_file(file, "en", translator)

            file = f"{source}/.hwaifs/text/py/{lib}/content.md"
            if os.path.exists(file):
               print(f"       Translating file = {file}")
               result_txt = api.translate_file(file, "en", translator)



if __name__ == '__main__':

   main()
