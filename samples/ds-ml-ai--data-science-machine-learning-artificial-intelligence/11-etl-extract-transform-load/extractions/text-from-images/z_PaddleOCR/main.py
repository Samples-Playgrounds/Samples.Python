"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install paddleocr
pip install paddlepaddle
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_text_extraction_from_images_PaddleOCR as api

import sys
import os
scriptpath = "../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *

sources = files_images

def main():
   for source in sources:
      print(f"PaddleOCR <- source = {source}")
      text = api.extract_text_to_file_from_image(source)
      print(f"  text = {text}")


if __name__ == '__main__':
    main()
