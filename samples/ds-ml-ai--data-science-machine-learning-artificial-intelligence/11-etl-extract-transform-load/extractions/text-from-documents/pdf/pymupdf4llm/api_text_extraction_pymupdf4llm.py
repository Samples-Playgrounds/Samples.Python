import pymupdf4llm
import os
from pathlib import Path


def extract_markdown_to_file_from_pdf_document (source: str) -> str:

    result_md = pymupdf4llm.to_markdown(source)

    directory = f"{source}.hwaifs/text/python/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}pymupdf4llm.md", "w") as f:
        f.write(result_md) 

    return result_md

def extract_markdown_to_file_from_office_doc_docx_document (source: str) -> str:

    result_md = pymupdf4llm.to_markdown(source)

    directory = f"{source}.hwaifs/text/python/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}pymupdf4llm.md", "w") as f:
        f.write(result_md) 

    return result_md
