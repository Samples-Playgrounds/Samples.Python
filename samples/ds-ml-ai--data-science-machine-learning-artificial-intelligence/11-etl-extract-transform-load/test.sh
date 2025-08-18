#!/bin/bash


cd ./extractions/document/docling/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/document/markitdown/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/document/PyMuPDF/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/document/PyPDF2/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/document/pymupdf4llm/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/document/unstructured/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -




