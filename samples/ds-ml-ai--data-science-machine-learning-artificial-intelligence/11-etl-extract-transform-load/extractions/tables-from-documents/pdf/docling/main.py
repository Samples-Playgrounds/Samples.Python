"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install opencv-python
pip install docling pandas
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""


import api_table_extraction_docling as api

import sys
import os
scriptpath = "../../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *


def main():
   for source in sources:
      if source.endswith(".pdf"):
         print(f"docling <- source = {source}")
         api.extract_tables_to_files_from_pdf_document(source)


if __name__ == '__main__':
    main()
