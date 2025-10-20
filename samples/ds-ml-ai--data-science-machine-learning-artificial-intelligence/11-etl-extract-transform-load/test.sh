#!/bin/bash


cd ./extractions/text/pdf/docling/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install docling
pip install docling[vlm]
pip install --upgrade pip
python main.py
cd -

cd ./extractions/text/pdf/marker/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install 'marker-pdf[full]'
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text/pdf/markitdown/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text/pdf/PyMuPDF/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text/pdf/PyPDF2/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text/pdf/pymupdf4llm/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text/pdf/unstructured/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text/pdf/pdfplumber/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text/pdf/pdfminer.six/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

# cd ./extractions/text/pdf/marker/
# rm -fr .venv __pycache__ 
# rm *.pyc
# python -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt
# pip install --upgrade pip
# pip install -r requirements.txt
# python main.py
# cd -



