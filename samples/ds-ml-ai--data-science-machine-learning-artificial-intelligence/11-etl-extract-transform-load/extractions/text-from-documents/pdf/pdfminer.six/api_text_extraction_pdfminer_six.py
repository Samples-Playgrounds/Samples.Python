import os
from pathlib import Path
from pdfminer.high_level import extract_text

def extract_text_to_file_from_pdf_document (source: str) -> str:

    result_txt = extract_text(source)

    directory = f"{source}.hwaifs/text/python/pdfminer_six/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.txt", "w") as f:
        f.write(result_txt)

    return result_txt

