#!/bin/bash

LIBRARY=pdfplumbers
figlet $LIBRARY
figlet start

pwd

deactivate
rm -fr .venv/ __pycache__/
rm *.pyc


python -m venv .venv
source .venv/bin/activate

pip install pdfplumber 
pip install pandas
pip install tabulate
pip install openpyxl

pip install timer
pip install codetiming

pip freeze > requirements.txt


python main.py

pwd
figlet stop
figlet $LIBRARY
