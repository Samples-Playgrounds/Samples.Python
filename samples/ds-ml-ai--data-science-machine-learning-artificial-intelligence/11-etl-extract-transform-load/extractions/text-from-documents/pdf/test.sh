#!/bin/bash

sys_term_clean_screen_and_buffer

ls -1 > list.md

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
pdfium2
# OCR based => slower
marker
pytesseract
# NOT working yet - ERRORS
# z_pymupdf4llm-c
# z_deepdoctection-pytorch
# z_deepdoctection-tensorflow
# NOT working yet - WIP 
# z_extractous
# z_multilingual-pdf2text
# z_pdf2text
# z_pypdf
# z_simple-pdf2text
# z_slate
# z_tika
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
