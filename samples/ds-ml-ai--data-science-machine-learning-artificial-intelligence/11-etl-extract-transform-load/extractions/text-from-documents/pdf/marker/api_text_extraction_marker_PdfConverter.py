import os
from pathlib import Path
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

def extract_text_to_file_from_pdf_document (source: str) -> str:
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )
    rendered = converter(source)
    result_md, _, images = text_from_rendered(rendered)

    directory = f"{source}.hwaifs/text/python/marker/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.md", "w") as f:
        f.write(result_md)

    return result_md

