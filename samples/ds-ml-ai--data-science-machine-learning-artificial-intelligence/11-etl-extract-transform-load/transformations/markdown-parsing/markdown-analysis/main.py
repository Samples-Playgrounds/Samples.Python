"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install markdown-analysis
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_parse_analyze_markdown_mrkdwn_analysis as api


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
      #print(f"mrkdwn_analysis <- source = {source}")
      for p in [
                  "text/py/pymupdf4llm/content.md",
                  "text/py/markitdown/content.md",
                  "text/py/docling/content.md",
                  "text/py/docling/content.filetype-agnostic.md",
                  "text/py/marker/content.md"
               ]:
         file = f"{source}.hwaifs/{p}"
         print(f"mrkdwn_analysis <- source = {file}")
         api.api_parse_analyze_markdown_mrkdwn_analysis(file)


if __name__ == '__main__':
    main()
