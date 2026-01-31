"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install keras-ocr
pip install tensorflow-metal
pip install tensorflow-macos

pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_text_extraction_from_images_keras_ocr as api

import sys
import os
scriptpath = "../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *

sources = files_images_web

def main():

    for source in sources:
        print(f"keras-ocr <- source = {source}")
        text = api.extract_text_to_file_from_image(source)
        print(f"  text = {text}")

    # Get a set of three example images
    sources = [
        keras_ocr.tools.read(url) for url in files_images_web
    ]



    #   for img in images:
    #      print(f"keras-ocr <- source = {source}")
    #      text = api.extract_text_to_file_from_image(source)
    #      print(f"  text = {text}")




if __name__ == '__main__':
    main()
