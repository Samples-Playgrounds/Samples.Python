import PyPDF2
import pytesseract
from PIL import Image

print("Environment setup successful!")

from PyPDF2 import PdfReader

# document per local path or URL
source = "/Volumes/FAT_VERB/learning/topics/security/threat-modelling/effectivethreatinvestigationforsocanalysts.pdf"
# "https://arxiv.org/pdf/2408.09869"  
# /Volumes/FAT_VERB/learning/topics/security/threat-modelling/threatmodeling.pdf

reader = PdfReader(source)
print(f"Number of pages: {len(reader.pages)}")

for page in reader.pages:
    print(page.extract_text())
