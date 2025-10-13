"""
deactivate
rm -fr .venv/ __pycache__/
"""
"""
python -m venv .venv
source .venv/bin/activate
pip install pdfplumber pandas
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_pdfplumber as api

# document per local path or URL
sources = [
   "/Users/moljac/Downloads/HRVATSKA AUTOCESTA D.O.O..pdf",
#   "/Users/moljac/Downloads/20250913/Zapisnik OS NZG K-226-2022-48 od 12.02.2024. - Nastavak glavne rasprave dana 12.02.2024. u 10_00 sati.pdf",
#   "../../../../../../../data/pravno/zakoni/zakon_o_sportskoj_inspekciji_nn_86_12.pdf",
#   "../../../../../../../data/pravno/zakoni/kazneni-zakon.docx",
#   "../../../../../../../data/pravno/zakoni/zakon-o-sportu-NN-19-16.pdf",
#   "../../../../../../../data/pravno/zakoni/zakon-o-sportu-2022.pdf",
#   "../../../../../../../data/pravno/zakoni/Kazneni-zakon.pdf",
#   "../../../../../../../data/pravno/zakoni/55-4.pdf",
#   "../../../../../../../data/pravno/satuti/hjs/status-HJS-a-2024.pdf",
#   "../../../../../../../data/pravno/satuti/hoo/Statut-HOO-a_procisceni-tekst_srpanj-2024.pdf",
#   "../../../../../../../data/pravno/satuti/gnk-dinamo/Nacrt+Prijedloga+Statuta+GNK+Dinamo.pdf",
#   "../../../../../../../data/pravno/satuti/gnk-dinamo/Prijedlog_Statuta_GNK_Dinamo_finalno_20250811_za+IO.pdf",
#   "../../../../../../../data/pravno/satuti/gnk-dinamo/statut-dinamo.2023.pdf",
#   "../../../../../../../data/pravno/satuti/gnk-dinamo/O Statutu_250814_100408.pdf",
#   "../../../../../../../data/pravno/dokumenti/hjs-zppi-2023-rjesenje.2.600dpi.compressed.pdf",
#   "../../../../../../../data/pravno/dokumenti/Rješenje - odbijanje zahtjeva Miljenko CVJETKO - 18.8.2025. .pdf"

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
      api.extract_tables_to_files(source)


