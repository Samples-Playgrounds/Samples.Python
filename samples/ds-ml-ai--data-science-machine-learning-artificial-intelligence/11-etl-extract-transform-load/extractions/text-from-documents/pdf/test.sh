#!/bin/bash


figlet docling
cd ./docling/
source ./test.sh
cd ..

figlet markitdown
cd ./markitdown/
source ./test.sh
cd ..

figlet minecart
cd ./minecart/
source ./test.sh
cd ..

figlet pdfminer.six
cd ./pdfminer.six/
source ./test.sh
cd ..

figlet pdfplumber
cd ./pdfplumber/
source ./test.sh
cd ..

figlet PyMuPDF
cd ./PyMuPDF/
source ./test.sh
cd ..

figlet pymupdf4llm
cd ./pymupdf4llm/
source ./test.sh
cd ..

figlet PyPDF2
cd ./PyPDF2/
source ./test.sh
cd ..

figlet unstructured
cd ./unstructured/
source ./test.sh
cd ..

figlet marker
cd ./marker/
source ./test.sh
cd ..

figlet pytesseract
cd ./pytesseract/
source ./test.sh
cd ..
