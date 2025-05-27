# python3.13 -m venv .venv
# source .venv/bin/activate
# pip3.13 install docling
# pip3.13 freeze > requirements.txt
# pip3.13 install -r requirements.txt
# python3.13 convert.py

import api

# document per local path or URL
source = "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf"
#source = "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#source = "https://arxiv.org/pdf/2408.09869"  

resuld_txt = api.covert_pdf_file_to_text(source)
resuld_md = api.covert_pdf_file_to_text(source)

print(resuld_txt)
print(resuld_md)
# save to file
print(f"python: docling.document_converter save {source}.docling.md")
# with open(f"{source}.docling.md", "w") as f:
#    f.write(result_md) 

