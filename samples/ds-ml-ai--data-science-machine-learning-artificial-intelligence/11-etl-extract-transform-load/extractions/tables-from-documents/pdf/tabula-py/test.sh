#!/bin/bash

deactivate
rm -fr .venv/ __pycache__/
rm *.pyc



python -m venv .venv
source .venv/bin/activate

pip install tabula-py
pip install tabula-py[jpype]
pip install jpype1
pip install pandas
pip install tabulate
pip install openpyxl

pip install timer
pip install codetiming

pip freeze > requirements.txt


python main.py
