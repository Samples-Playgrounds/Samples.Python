#!/bin/bash

EXTRACTORS=\
"
PyMuPDF-fitz
pypdf-PyPDF2
pikepdf
minecart
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
done



figlet "==========="
for i in $(seq 1 10);
do
    echo -en "\007"
    say "I'm done"
done
