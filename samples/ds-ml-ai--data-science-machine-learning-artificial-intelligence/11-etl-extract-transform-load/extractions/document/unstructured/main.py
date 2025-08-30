"""
python3.13 -m venv .venv
source .venv/bin/activate
pip3.13 install "unstructured[all-docs]"
pip3.13 freeze > requirements.txt
pip3.13 install -r requirements.txt
python3.13 main.py
"""

import api

# document per local path or URL
sources = [
   "../../../../../../data/pravno/zakoni/zakon_o_sportskoj_inspekciji_nn_86_12.pdf",
   "../../../../../../data/pravno/zakoni/kazneni-zakon.docx",
   "../../../../../../data/pravno/zakoni/zakon-o-sportu-NN-19-16.pdf",
   "../../../../../../data/pravno/zakoni/zakon-o-sportu-2022.pdf",
   "../../../../../../data/pravno/zakoni/Kazneni-zakon.pdf",
   "../../../../../../data/pravno/zakoni/55-4.pdf",
   "../../../../../../data/pravno/satuti/hjs/status-HJS-a-2024.pdf",
   "../../../../../../data/pravno/satuti/hoo/Statut-HOO-a_procisceni-tekst_srpanj-2024.pdf",
   "../../../../../../data/pravno/satuti/gnk-dinamo/Nacrt+Prijedloga+Statuta+GNK+Dinamo.pdf",
   "../../../../../../data/pravno/satuti/gnk-dinamo/Prijedlog_Statuta_GNK_Dinamo_finalno_20250811_za+IO.pdf",
   "../../../../../../data/pravno/satuti/gnk-dinamo/statut-dinamo.2023.pdf",
   "../../../../../../data/pravno/satuti/gnk-dinamo/O Statutu_250814_100408.pdf",
   "../../../../../../data/pravno/dokumenti/hjs-zppi-2023-rjesenje.2.600dpi.compressed.pdf",
   "../../../../../../data/pravno/dokumenti/Rješenje - odbijanje zahtjeva Miljenko CVJETKO - 18.8.2025. .pdf"
#  "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/microsoft/dotnet/maui/NET_MAUI_in_Action.pdf",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/microsoft/dotnet/maui/mvvmpatterninnetmaui.pdf",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/doc_files/13.\ Funkcionalna\ procjena\ pokreta.docx",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/doc_files/14.\ Literatura.docx",
]
#  "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#   "https://arxiv.org/pdf/2408.09869"


for source in sources:
   if source.endswith(".pdf"):

      result_txt = api.covert_pdf_file_to_text(source)
      print(result_txt)

      # save to file
      print(f"python: unstructured save {source}.unstructured.1.txt")
      with open(f"{source}.unstructured.1.txt", "w") as f:
         f.write(result_txt) 




