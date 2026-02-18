"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install pdf2image
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_extract_images_pdf2image as api

root="../../../../../../../data"

import sys
import os
scriptpath = "../../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *

sources = files_documents_pdfs


def main():
   for source in files_documents_pdfs:
      if source.endswith(".pdf"):
         print(f"pdf2image <- source = {source}")
         api.extract_pages_to_images(source)


if __name__ == '__main__':
    main()
