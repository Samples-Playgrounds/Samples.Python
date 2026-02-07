"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate

pip install pytesseract
pip install opencv-python

pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
# export TESSDATA_PREFIX="/opt/homebrew/share/tessdata/"
python main.py
"""

import api_text_extraction_from_images_pytesseract as api


import sys
import os
scriptpath = "../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *


def main():

   sources = files_images

   for source in sources:
      print(f"pytesseract <- source = {source}")
      text = api.extract_text_to_file_from_image(source)
      print(f"  text = {text}")

   

if __name__ == '__main__':
    main()
