#!/bin/bash

LIBRARY=kreuzberg
figlet $LIBRARY
figlet start

pwd

deactivate
rm -fr .venv/ __pycache__/
rm *.pyc


python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

pip install kreuzberg
pip install "kreuzberg[easyocr]"
pip install "kreuzberg[paddleocr]"
pip install "kreuzberg[all]"

pip install timer
pip install codetiming

pip freeze > requirements.txt


python main.py

pwd
figlet stop
figlet $LIBRARY
