#!/bin/bash

LIBRARY=docling
figlet $LIBRARY
figlet start

pwd

deactivate
rm -fr .venv/ __pycache__/
rm *.pyc


python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

pip install docling
pip install docling[vlm]
pip install opencv-python

pip install timer
pip install codetiming

pip freeze > requirements.txt


python main.py

pwd
figlet stop
figlet $LIBRARY
