# python3.13 -m venv .venv
# source .venv/bin/activate
# pip3.13 install pymupdf4llm
# pip3.13 freeze > requirements.txt
# pip3.13 install -r requirements.txt
# python3.13 main.py

import api

import api

# document per local path or URL
sources = [
   "../../../../../data/pravno/zakoni/zakon_o_sportskoj_inspekciji_nn_86_12.pdf",
   "../../../../../data/pravno/zakoni/kazneni-zakon.docx",
   "../../../../../data/pravno/zakoni/zakon-o-sportu-NN-19-16.pdf",
   "../../../../../data/pravno/zakoni/zakon-o-sportu-2022.pdf",
   "../../../../../data/pravno/zakoni/Kazneni-zakon.pdf",
   "../../../../../data/pravno/zakoni/55-4.pdf",
   "../../../../../data/pravno/satuti/hjs/status-HJS-a-2024.pdf",
   "../../../../../data/pravno/satuti/hoo/Statut-HOO-a_procisceni-tekst_srpanj-2024.pdf",
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
      result_md = api.covert_pdf_file_to_markdown(source)
      print(result_md)

      # save to file
      print(f"python: pymupdf4llm save {source}.pymupdf4llm.1.md")
      with open(f"{source}.pymupdf4llm.1.md", "w") as f:
         f.write(result_md) 


      # now work with the markdown text, e.g. store as a UTF8-encoded file
      import pathlib
      print(f"python: pymupdf4llm save {source}.pymupdf4llm.2.md")
      pathlib.Path(f"{source}.pymupdf4llm.2.md").write_bytes(result_md.encode())
