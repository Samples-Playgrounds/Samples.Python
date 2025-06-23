import api

# document per local path or URL
# source = "/Volumes/FAT_VERB/learning/topics/security/threat-modelling/effectivethreatinvestigationforsocanalysts.pdf"
# "https://arxiv.org/pdf/2408.09869"  
# document per local path or URL
source = "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf"
#source = "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#source = "/Volumes/FAT_VERB/learning/topics/security/threat-modelling/threatmodeling.pdf
#source = "https://arxiv.org/pdf/2408.09869"  

result_txt = api.covert_pdf_file_to_text(source)

print(result_txt)

# save to file
print(f"python: docling.document_converter save {source}.PyMuPDF-fitz.txt")
with open(f"{source}.PyMuPDF-fitz.txt", "w") as f:
   f.write(result_txt) 
