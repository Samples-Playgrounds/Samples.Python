"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install epub2txt
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_text_extraction_epub2txt as api

import sys
import os
scriptpath = "../../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *

sources = files_documents_epubs

def main():
   for source in sources:
      print(f"EbookLib <- source = {source}")
      result_txt = api.extract_text_to_file_from_epub_document(source)

if __name__ == '__main__':
    main()

