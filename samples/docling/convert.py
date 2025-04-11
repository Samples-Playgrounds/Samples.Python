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

def covert_docling(source: str) -> str:
    converter = DocumentConverter()
    print(f"Docling load {source}")
    result = converter.convert(source)
    resuld_md = result.document.export_to_markdown()  # output: "## Docling Technical Report[...]"
    print(resuld_md)
    # save to file
    print(f"Docling save {source}.md")
    with open(f"{source}.md", "w") as f:
        f.write(resuld_md)

    return resuld_md


covert_docling(source)
