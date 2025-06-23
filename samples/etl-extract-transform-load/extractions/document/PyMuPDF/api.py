import fitz  # PyMuPDF

def covert_pdf_file_to_text (source: str) -> str:
    doc = fitz.open(source)
    result_txt = ""
    for page in doc:
        result_txt = result_txt +  page.get_text("text")

    return result_txt

