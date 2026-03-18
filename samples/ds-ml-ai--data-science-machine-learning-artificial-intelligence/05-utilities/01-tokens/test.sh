#!/bin/bash

sys_term_clean_screen_and_buffer

ls -d1 */ > list.md

EXTRACTORS=\
"
01-standard-library-split
# 02-nltk-word_tokenize
21-tiktoken
# 22-hf-huggingface
# 23-iree-tokenizer
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
