#!/bin/bash


figlet docling
cd ./docling/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install docling
pip install docling[vlm]
pip install opencv-python
pip install --upgrade pip
python main.py
cd -

figlet marker
cd ./marker/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install 'marker-pdf[full]'
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

figlet markitdown
cd ./markitdown/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install markitdown[all]
pip install 'markitdown[pdf, docx, pptx]'
pip install 'markitdown[pdf, docx, pptx, xslx, xsl, outlook, audio-transcription, youtube-transcription]'
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

figlet minecart
cd ./minecart/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install minecart
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

figlet pdfminer.six
cd ./pdfminer.six/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install pdfminer.six
pip install 'pdfminer.six[image]'
pip install --upgrade pip
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
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

figlet PyMuPDF
cd ./PyMuPDF/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install PyMuPDF
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

figlet pymupdf4llm
cd ./pymupdf4llm/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install pymupdf4llm
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

figlet PyPDF2
cd ./PyPDF2/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install PyPDF2
pip install pytesseract
pip install Pillow
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

figlet pytesseract
cd ./pytesseract/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

figlet unstructured
cd ./unstructured/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install "unstructured[all-docs]"
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -
