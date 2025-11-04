# python3.13 -m venv .venv
# source .venv/bin/activate
# pip3.13 install translators
# pip3.13 freeze > requirements.txt
# pip3.13 install -r requirements.txt
# python3.13 main.py

import api_translate_translators as api


root="/Users/Shared/Projects/e/learning/books/topics/sports/Moljac_Knjiga/doc_files/"

# document per local path or URL
sources = [
   f"{root}/0. Naslovnica.docx"
   f"{root}/1. Uvod.docx"
   f"{root}/10. Transverzalna dimenzionalnost skeleta.docx"
   f"{root}/11. Volumen i masa tijela.docx"
   f"{root}/12. Potkožno masno tkivo.docx"
   f"{root}/13. Funkcionalna procjena pokreta.docx"
   f"{root}/14. Literatura.docx"
   f"{root}/2. Testovi jakosti.docx"
   f"{root}/3. Testovi brzine.docx"
   f"{root}/4. Testovi izdrzljivosti.docx"
   f"{root}/5. Testovi koordinacije.docx"
   f"{root}/6. Testovi agilnosti.docx"
   f"{root}/7. Testovi ravnoteze.docx"
   f"{root}/8. Testovi fleksibilnosti.docx"
   f"{root}/9. Longitudinalna dimenzionalnost skeleta.docx"
   f"{root}/Sadržaj.docx"
]




# document per local path or URL



source = "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf.docling.cleaned.md"
# source = "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf.unstructured.1.md"
#source = "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#source = "https://arxiv.org/pdf/2408.09869"  

result_txt = api.translate_text(source, "en", "google")

print(result_txt)

# save to file
print(f"python: save {source}.translators-google.en.1.md")
with open(f"{source}.translators-google.en.1.md", "w") as f:
   f.write(result_txt) 


# now work with the markdown text, e.g. store as a UTF8-encoded file
import pathlib
print(f"python: save {source}..translators-google.en.2.md")
pathlib.Path(f"{source}.translators-google.en.2.md").write_bytes(result_txt.encode())


result_txt = api.translate_text(source, "en", "microsoft")

print(result_txt)

# save to file
print(f"python: save {source}.translators-microsoft.en.1.md")
with open(f"{source}.translators-microsoft.en.1.md", "w") as f:
   f.write(result_txt) 


# now work with the markdown text, e.g. store as a UTF8-encoded file
import pathlib
print(f"python: save {source}..translators-microsoft.en.2.md")
pathlib.Path(f"{source}.translators-microsoft.en.2.md").write_bytes(result_txt.encode())

