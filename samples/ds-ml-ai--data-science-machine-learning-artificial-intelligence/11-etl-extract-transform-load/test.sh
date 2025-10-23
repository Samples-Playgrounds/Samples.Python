#!/bin/bash


cd ./extractions/text-from-documents/pdf/docling/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install docling
pip install docling[vlm]
pip install --upgrade pip
python main.py
cd -

cd ./extractions/text-from-documents/pdf/marker/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install 'marker-pdf[full]'
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text-from-documents/pdf/markitdown/
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

cd ./extractions/text-from-documents/pdf/minecart/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install minecart
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text-from-documents/pdf/pdfminer.six/
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

cd ./extractions/text-from-documents/pdf/pdfplumber/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install pdfplumber
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -


cd ./extractions/text-from-documents/pdf/PyMuPDF/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install PyMuPDF
pip install --upgrade pip
pip install -r requirements.txt
python main.pyw
cd -

cd ./extractions/text-from-documents/pdf/pymupdf4llm/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install pymupdf4llm
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text-from-documents/pdf/PyPDF2/
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

cd ./extractions/text-from-documents/pdf/pytesseract/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -

cd ./extractions/text-from-documents/pdf/unstructured/
rm -fr .venv __pycache__ 
rm *.pyc
python -m venv .venv
source .venv/bin/activate
pip install "unstructured[all-docs]"
pip install --upgrade pip
pip install -r requirements.txt
python main.py
cd -
