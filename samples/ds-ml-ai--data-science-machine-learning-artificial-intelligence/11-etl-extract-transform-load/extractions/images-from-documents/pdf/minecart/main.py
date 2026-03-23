"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install minecart
pip install Pillow
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_image_extraction_minecart as api

import sys
import os
scriptpath = "../../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *


def main():
   for source in sources:
      if source.endswith(".pdf"):
         print(f"minecart <- source = {source}")
         api.extract_images_from_pdf_to_files(source)

if __name__ == '__main__':
    main()

