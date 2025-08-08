#!/bin/bash


cd ./extractions/document/docling/
python main.py
cd -

cd ./extractions/document/unstrucutred/
python main.py
cd -

cd ./extractions/document/markitdown/
python main.py
cd -

cd ./extractions/document/PyMuPDF/
python main.py
cd -

cd ./extractions/document/pymupdf4llm/
python main.py
cd -

