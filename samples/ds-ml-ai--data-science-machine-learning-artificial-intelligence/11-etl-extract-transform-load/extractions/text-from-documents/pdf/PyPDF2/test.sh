#!/bin/bash

deactivate
rm -fr .venv/ __pycache__/
rm *.pyc



python -m venv .venv
source .venv/bin/activate

pip install PyPDF2
pip install pytesseract
pip install Pillow

pip install timer
pip install codetiming

pip freeze > requirements.txt


python main.py
