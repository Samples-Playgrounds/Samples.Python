#!/bin/bash

figlet gmft
cd ./gmft/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install transformers
pip install torch torchvision
pip install gmft
pip install openpyxl
pip install --upgrade pip
python main.py
cd -

figlet tabula-py
cd ./tabula-py/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install tabula-py
pip install tabula-py[jpype]
pip install tabula-py
pip install tabula-py[jpype]
pip install jpype1
pip install pandas
pip install tabulate
pip install openpyxl
pip install --upgrade pip
python main.py
cd -

figlet docling
cd ./docling/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install opencv-python
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
pip install pdfplumber 
pip install pandas
pip install tabulate
pip install openpyxl
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


figlet marker
cd ./marker/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install legacy-cgi
pip install 'marker-pdf[full]'
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -
