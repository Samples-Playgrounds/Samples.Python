"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install marko
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_parse_analyze_markdown_marko as api


import sys  
import os
scriptpath = "../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *

root="../../../../../data/"

sources = files_documents_pdfs

def main():
   for source in files_documents_pdfs:
      source = source.replace(
                                 "../../../../../../../data/", 
                                 "../../../../../../data/"
                              )
      print(120 * "=")
      print(f"marko <- source = {source}")
      for file in [
                     "text/py/pymupdf4llm/content.md",
                     "text/py/docling/content.md",
                     "text/py/docling/content.filetype-agnostic.md",
                     "text/py/marker/content.md",
                     "text/py/MarkItDown/content.txt",
                  ]:
         print(100 * ".")
         file = f"{source}.hwaifs/{file}"
         print(f"                = {file}")
         paragraphs = api.api_parse_analyze_markdown_marko(file)
         print(f"marko <- paragraphs = {paragraphs}")


if __name__ == '__main__':
    main()
