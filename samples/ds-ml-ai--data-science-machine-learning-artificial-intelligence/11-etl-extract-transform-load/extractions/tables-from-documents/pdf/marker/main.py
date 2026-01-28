"""
rm -fr .venv __pycache__ *.pyc
python -m venv .venv
source .venv/bin/activate
pip install legacy-cgi
pip install 'marker-pdf[full]'
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_table_extraction_marker_TableConverter as api

import sys
import os
scriptpath = "../../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *


def main():
   for source in sources:
      if source == "/Users/Shared/Projects/e/learning/books/topics/sports/Moljac_Knjiga/doc_files/13. Funkcionalna procjena pokreta.docx":
         continue
         
      print(f"marker <- source = {source}")
      api.extract_tables_to_files_from_pdf_document(source)

if __name__ == '__main__':
    main()


