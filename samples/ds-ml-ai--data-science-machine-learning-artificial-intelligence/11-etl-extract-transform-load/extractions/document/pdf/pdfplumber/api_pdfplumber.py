from pdfminer.high_level import extract_text

def covert_pdf_file_to_markdown (source: str) -> str:

    text = extract_text(source)

    return text

