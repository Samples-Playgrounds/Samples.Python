import fitz  # PyMuPDF

import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

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

#@timer()
def extract_text_to_file_from_pdf_document (source: str) -> str:

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    doc = fitz.open(source)
    result_txt = ""
    for page in doc:
        result_txt = result_txt + page.get_text("text")

    directory = f"{source}.hwaifs/text/python/PyMuPDF_fitz/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.txt", "w") as f:
        f.write(result_txt) 

    #---------------------------------------------------------------------------
    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name" : "extract_text_to_file_from_any_document",
        "time_start_1": time_start_1,
        "time_end_1": time_stop_1,
        "time_total_1": time_total_1,
        "time_start_2": time_start_2,
        "time_end_2": time_stop_2,
        "time_total_2": time_total_2,
        "time_start_3": time_start_3,
        "time_end_3": time_stop_3,
        "time_total_3": time_total_3,
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.python.json", "w") as f:
        f.write(json.dumps(times, indent=4))
    #---------------------------------------------------------------------------

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
