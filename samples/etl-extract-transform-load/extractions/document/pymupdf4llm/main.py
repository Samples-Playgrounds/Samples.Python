# python3.13 -m venv .venv
# source .venv/bin/activate
# pip3.13 install pymupdf4llm
# pip3.13 freeze > requirements.txt
# pip3.13 install -r requirements.txt
# python3.13 main.py

import api

# document per local path or URL
source = "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf"
#source = "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#source = "https://arxiv.org/pdf/2408.09869"  

result_md = api.covert_pdf_file_to_markdown(source)

print(result_md)

# save to file
print(f"python: docling.document_converter save {source}.pymupdf4llm.1.md")
with open(f"{source}.pymupdf4llm.md", "w") as f:
   f.write(result_md) 


# now work with the markdown text, e.g. store as a UTF8-encoded file
import pathlib
print(f"python: docling.document_converter save {source}.pymupdf4llm.2.md")
pathlib.Path(f"{source}.pymupdf4llm.md").write_bytes(result_md.encode())


