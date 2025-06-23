import api

# document per local path or URL
source = "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf"
#source = "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#source = "https://arxiv.org/pdf/2408.09869"  

result_md = api.covert_pdf_file_to_markdown(source)

print(result_md)

# save to file
print(f"python: PyPDF2 save {source}.PyPDF2.1.md")
with open(f"{source}.PyPDF2.md", "w") as f:
   f.write(result_md) 
