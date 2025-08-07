# python3.13 -m venv .venv
# source .venv/bin/activate
# pip3.13 install "llama_index"
# pip3.13 freeze > requirements.txt

import api

# document per local path or URL
file="mit.txt"

#  "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#   "https://arxiv.org/pdf/2408.09869"

from llama_index.readers.file import FlatReader
from pathlib import Path

md_docs = FlatReader().load_data(Path(file))

nodes = api.split_text(md_docs, 2000, 20)

for node in nodes:
   print(f"============================================================================")
   print(node)

