#!/bin/bash


figlet docling
cd ./docling/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install docling pandas
pip install --upgrade pip
python main.py
cd -

figlet camelot
cd ./camelot/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install "camelot-py[base]"
pip install -r requirements.txt
python main.py
cd -

figlet pdfplumber
cd ./pdfplumber/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install pdfplumber pandas
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

figlet pdftables
cd ./pdftables/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install pdftables
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -
