try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

import pytesseract
import PyPDF2

from PyPDF2 import PdfReader

def covert_pdf_file_to_markdown (source: str) -> str:
    reader = PdfReader(source)
    result_md = ""
    for page in reader.pages:
        result_md = result_md + page.extract_text()

    return result_md