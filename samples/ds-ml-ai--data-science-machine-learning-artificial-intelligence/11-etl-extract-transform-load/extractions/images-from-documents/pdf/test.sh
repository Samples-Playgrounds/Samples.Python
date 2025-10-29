#!/bin/bash


figlet PyMuPDF-fitz
cd ./PyMuPDF-fitz/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install PyMuPDF
pip install --upgrade pip
python main.py
cd -

figlet pypdf-PyPDF2
cd ./pypdf-PyPDF2/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install PyPDF2
pip install "PyPDF2[image]"
pip install -r requirements.txt
python main.py
cd -

figlet pikepdf
cd ./pikepdf/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install pikepdf
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ..