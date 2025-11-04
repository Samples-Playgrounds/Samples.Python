#!/bin/bash

figlet pdf2image
cd ./pdf2image/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install pdf2image
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -
