#!/bin/bash

LIBRARY=docTR
figlet $LIBRARY
figlet start

pwd

deactivate
rm -fr .venv/ __pycache__/
rm *.pyc


python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

pip install python-doctr
#pip install "python-doctr[viz,html,contrib]"

pip install timer
pip install codetiming

pip freeze > requirements.txt


python main.py

pwd
figlet stop
figlet $LIBRARY
