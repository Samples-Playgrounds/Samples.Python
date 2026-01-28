"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install "unstructured[all-docs]"
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_text_extraction_unstructured_partition_pdf as api

import sys
import os
scriptpath = "../../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *

def main():

   for source in sources:
      if source.endswith(".pdf"):
         print(f"unstructured <- source :  {source}")
         result_txt = api.extract_text_to_file_from_pdf_document(source)


if __name__ == '__main__':
    main()



