# python3.13 -m venv .venv
# source .venv/bin/activate
# pip3.13 install 'markitdown[pdf, docx, pptx, xslx, xsl, outlook, audio-transcription, youtube-transcription]'
# pip3.13 freeze > requirements.txt
# pip3.13 install -r requirements.txt
# python3.13 main.py

import api

# document per local path or URL
source = "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf"
#source = "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#source = "https://arxiv.org/pdf/2408.09869"  

result_md = api.covert_file_to_markdown(source)
print(result_md)

# save to file
print(f"python: docling.document_converter save {source}.markitdown_pdf.md")
with open(f"{source}.markitdown_pdf.md", "w") as f:
   f.write(result_md) 

source = "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/doc_files/0. Naslovnica.docx"

result_md = api.covert_file_to_markdown(source)
print(result_md)


# save to file
print(f"python: docling.document_converter save {source}.markitdown_docx.md")
with open(f"{source}.markitdown_docx.md", "w") as f:
   f.write(result_md) 


