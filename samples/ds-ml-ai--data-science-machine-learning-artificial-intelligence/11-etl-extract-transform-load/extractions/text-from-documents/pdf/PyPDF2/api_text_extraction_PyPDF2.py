try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract
import PyPDF2
import os
from pathlib import Path


from PyPDF2 import PdfReader

def extract_text_to_file_from_pdf_document (source: str) -> str:
    reader = PdfReader(source)
    result_txt = ""
    for page in reader.pages:
        result_txt = result_txt + page.extract_text()

    directory = f"{source}.hwaifs/text/python/PyPDF2/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.txt", "w") as f:
        f.write(result_txt) 

    return result_txt