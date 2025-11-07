#!/bin/bash

figlet text-from-docs
cd ./text-from-documents/
source ./test.sh
cd ..

figlet images-from-docs
cd ./images-from-documents/
source ./test.sh
cd ..

figlet tables-from-docs
cd ./tables-from-documents/
source ./test.sh
cd ..
