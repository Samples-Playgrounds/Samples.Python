import fitz  # PyMuPDF
import os
from pathlib import Path

# https://pymupdf.readthedocs.io/en/latest/how-to-open-a-file.html#supported-file-types
# Document Formats
# 
#     PDF 
#     
#     XPS 
#     EPUB 
#     MOBI 
#     FB2 
#     CBZ 
#     SVG 
#     TXT
# 
# Image Formats
# Input formats
#     JPG/JPEG,
#     PNG,
#     BMP,
#     GIF,
#     TIFF,
#     PNM,
#     PGM,
#     PBM,
#     PPM,
#     PAM,
#     JXR,
#     JPX/JP2,
#     PSD
# Output formats
#     JPG/JPEG,
#     PNG,
#     PNM,
#     PGM,
#     PBM,
#     PPM,
#     PAM,
#     PSD,
#     PS


def extract_text_to_file_from_pdf_document (source: str) -> str:
    doc = fitz.open(source)
    result_txt = ""
    for page in doc:
        result_txt = result_txt + page.get_text("text")

    directory = f"{source}.hwaifs/text/python/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}PyMuPDF-fitz.txt", "w") as f:
        f.write(result_txt) 

    return result_txt

# NOT   available in PyMuPDF
#       available in pymupdfllm

# import pymupdf
# from pymupdf_rag import to_markdown  # import Markdown converter
# 
# def covert_pdf_file_to_markdown (source: str) -> str:
#     doc = fitz.open(source)
#     result_md = ""
#     for page in doc:
#         result_md = result_md +  to_markdown(doc, page_number=page.number)
# 
#     return result_md
