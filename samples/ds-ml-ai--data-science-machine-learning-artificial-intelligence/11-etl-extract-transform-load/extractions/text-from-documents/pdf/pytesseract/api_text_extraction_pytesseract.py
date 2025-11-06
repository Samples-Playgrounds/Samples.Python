import pytesseract
from pdf2image import convert_from_path
import os
from pathlib import Path


def extract_text_to_file_from_pdf_document (source: str) -> str:
    pages = convert_from_path(source, 500)
    
    result_txt = ""
    for pageNum,imgBlob in enumerate(pages):
        result_txt = result_txt + pytesseract.image_to_string(imgBlob,lang='eng')

    directory = f"{source}.hwaifs/text/python/pytesseract/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.txt", "w") as f:
        f.write(result_txt) 

    return result_txt