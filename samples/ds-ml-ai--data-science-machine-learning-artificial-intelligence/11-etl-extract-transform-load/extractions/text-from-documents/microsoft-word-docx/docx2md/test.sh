#!/bin/bash

LIBRARY=docx2md
figlet $LIBRARY
figlet start

pwd

deactivate
rm -fr .venv/ __pycache__/
rm *.pyc


python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

pip install docx2md

pip install orjson
pip install timer
pip install codetiming

pip freeze > requirements.txt


python main.py

pwd
figlet stop
figlet $LIBRARY
