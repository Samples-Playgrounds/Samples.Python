# python3.13 -m venv .venv
# source .venv/bin/activate
# pip3.13 install translators
# pip3.13 freeze > requirements.txt
# pip3.13 install -r requirements.txt
# python3.13 main.py

import api

# document per local path or URL
source = "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf.docling.cleaned.md"
# source = "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf.unstructured.1.md"
#source = "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#source = "https://arxiv.org/pdf/2408.09869"  

result_txt = api.translate_text(source, "en", "google")

print(result_txt)

# save to file
print(f"python: save {source}.deep-translator-google.en.1.md")
with open(f"{source}.deep-translator-google.en.1.md", "w") as f:
   f.write(result_txt) 


# now work with the markdown text, e.g. store as a UTF8-encoded file
import pathlib
print(f"python: save {source}..deep-translator-google.en.2.md")
pathlib.Path(f"{source}.deep-translator-google.en.2.md").write_bytes(result_txt.encode())



result_txt = api.translate_text(source, "en", "microsoft")

print(result_txt)

# save to file
print(f"python: save {source}.deep-translator-microsoft.en.1.md")
with open(f"{source}.deep-translator-microsoft.en.1.md", "w") as f:
   f.write(result_txt) 


# now work with the markdown text, e.g. store as a UTF8-encoded file
import pathlib
print(f"python: save {source}..deep-translator-microsoft.en.2.md")
pathlib.Path(f"{source}.deep-translator-microsoft.en.2.md").write_bytes(result_txt.encode())




result_txt = api.translate_text(source, "en", "pons")

print(result_txt)

# save to file
print(f"python: save {source}.deep-translator-pons.en.1.md")
with open(f"{source}.deep-translator-pons.en.1.md", "w") as f:
   f.write(result_txt) 


# now work with the markdown text, e.g. store as a UTF8-encoded file
import pathlib
print(f"python: save {source}..deep-translator-pons.en.2.md")
pathlib.Path(f"{source}.deep-translator-pons.en.2.md").write_bytes(result_txt.encode())





result_txt = api.translate_text(source, "en", "mymemory")

print(result_txt)

# save to file
print(f"python: save {source}.deep-translator-mymemory.en.1.md")
with open(f"{source}.deep-translator-mymemory.en.1.md", "w") as f:
   f.write(result_txt) 


# now work with the markdown text, e.g. store as a UTF8-encoded file
import pathlib
print(f"python: save {source}..deep-translator-mymemory.en.2.md")
pathlib.Path(f"{source}.deep-translator-mymemory.en.2.md").write_bytes(result_txt.encode())







result_txt = api.translate_text(source, "en", "yandex")

print(result_txt)

# save to file
print(f"python: save {source}.deep-translator-yandex.en.1.md")
with open(f"{source}.deep-translator-yandex.en.1.md", "w") as f:
   f.write(result_txt) 


# now work with the markdown text, e.g. store as a UTF8-encoded file
import pathlib
print(f"python: save {source}..deep-translator-yandex.en.2.md")
pathlib.Path(f"{source}.deep-translator-yandex.en.2.md").write_bytes(result_txt.encode())
