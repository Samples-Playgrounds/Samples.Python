#!/bin/bash

sys_term_clean_screen_and_buffer

EXTRACTORS=\
"
markitdown
pdfminer.six
docling
pdfplumber
PyMuPDF
pymupdf4llm
PyPDF2
unstructured
# OCR based => slower
marker
pytesseract
# NOT working yet - ERRORS
# pymupdf4llm-c
# deepdoctection-pytorch
# deepdoctection-tensorflow
# NOT working yet - WIP 
# extractous
# multilingual-pdf2text
# pdf2text
# pdfium2
# pypdf
# simple-pdf2text
# slate
# tika
"


IFS=$'\n'
# ZSH does not split words by default (like other shells):
setopt sh_word_split

for EXTRACTOR in $EXTRACTORS
do
    if [[ $EXTRACTOR == "#"* ]]
    then
        echo "......................................................................"        
        echo $EXTRACTOR skipped
        continue
    fi

    cd $EXTRACTOR
    source ./test.sh
    cd ..
done


figlet "==========="
for i in $(seq 1 10);
do
    echo -en "\007"
    say "I'm done"
done
