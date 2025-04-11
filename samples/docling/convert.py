# python3.13 -m venv .venv
# source .venv/bin/activate
# pip3.13 install docling
# pip3.13 freeze > requirements.txt
# pip3.13 install -r requirements.txt
# python3.13 convert.py
from docling.document_converter import DocumentConverter

# document per local path or URL
source = "/Volumes/FAT_VERB/learning/topics/security/threat-modelling/effectivethreatinvestigationforsocanalysts.pdf"
# "https://arxiv.org/pdf/2408.09869"  
# /Volumes/FAT_VERB/learning/topics/security/threat-modelling/threatmodeling.pdf

converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"