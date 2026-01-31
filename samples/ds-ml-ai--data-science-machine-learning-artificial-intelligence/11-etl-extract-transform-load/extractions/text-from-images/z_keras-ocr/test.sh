#!/bin/bash

LIBRARY=keras-ocr
figlet $LIBRARY
figlet start

pwd

deactivate
rm -fr .venv/ __pycache__/
rm *.pyc


python -m venv .venv
source .venv/bin/activate

python3.13 -m venv tf-venv
source tf-venv/bin/activate
python -m pip install --upgrade pip
pip install tensorflow-macos tensorflow-metal

#brew install hdf5
#pip install tensorflow-macos
#pip install tensorflow-metal
#

pip install timer
pip install codetiming

pip freeze > requirements.txt


python main.py

pwd
figlet stop
figlet $LIBRARY

