"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install gTTS
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_tts_text_to_speech_gTTS as api

import sys
import os
scriptpath = "../../../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *


texts_simple = [
                     "Hi Moljac. What's up?",
                  ]


def main():

   for text in texts_simple:

      print(f"gTTS <- text = {text}")
      file_audio = api.speak(text)

      os.startfile(file_audio)


   for source in files_documents_pdfs:
      source = source.replace(
                                 "../../../../../../../data/", 
                                 "../../../../../../data/"
                              )
      print(120 * "=")
      print(f"gTTS <- source = {source}")
      for file in [
                     "text/py/pymupdf4llm/content.md",
                     "text/py/docling/content.md",
                     "text/py/docling/content.filetype-agnostic.md",
                     "text/py/marker/content.md",
                     "text/py/MarkItDown/content.txt",
                  ]:
         print(100 * ".")
         file = f"{source}.hwaifs/{file}"
         print(f"                = {file}")

         with open(file, 'r') as f:
            text = f.read()
      
         api.speak(text, "en")



if __name__ == '__main__':
    main()


