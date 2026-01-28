"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install pymupdf4llm-c 
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_text_extraction_pymupdf4llm_c as api

root="../../../../../../../data"
root_sports_book="/Users/Shared/Projects/e/learning/books/topics/sports/Moljac_Knjiga"
root_sports_reports_lab_kif="/Users/Shared/Projects/d/hw/apps/Ph4ct3x/gl/Ph4ct3x.Docs/users/lara/diagnostics/kif/"

import sys
import os
scriptpath = "../../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *


def main():

   for source in sources:
      if source.endswith(".pdf"):
         print(f"pytesseract <- source :  {source}")
         result_txt = api.extract_text_to_file_from_pdf_document(source)


if __name__ == '__main__':
    main()
