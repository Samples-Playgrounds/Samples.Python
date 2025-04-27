import fitz  # PyMuPDF

# document per local path or URL
source = "/Volumes/FAT_VERB/learning/topics/security/threat-modelling/effectivethreatinvestigationforsocanalysts.pdf"
# "https://arxiv.org/pdf/2408.09869"  
# /Volumes/FAT_VERB/learning/topics/security/threat-modelling/threatmodeling.pdf

doc = fitz.open(source)
for page in doc:
    print(page.get_text("text"))
