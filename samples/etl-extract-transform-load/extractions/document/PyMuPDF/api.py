import fitz  # PyMuPDF

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


def covert_pdf_file_to_text (source: str) -> str:
    doc = fitz.open(source)
    result_txt = ""
    for page in doc:
        result_txt = result_txt +  page.get_text("text")

    return result_txt

