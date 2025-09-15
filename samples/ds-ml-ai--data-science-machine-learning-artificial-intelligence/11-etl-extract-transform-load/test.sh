#!/bin/bash


cd ./extractions/document/pdf/docling/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/document/pdf/markitdown/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/document/pdf/PyMuPDF/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/document/pdf/PyPDF2/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/document/pdf/pymupdf4llm/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/document/pdf/unstructured/
rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -




