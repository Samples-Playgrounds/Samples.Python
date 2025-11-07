from marker.converters.table import TableConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

import json
from pathlib import Path

converter = TableConverter(
    artifact_dict=create_model_dict(),
)

def extract_tables_to_files_from_pdf_document (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/tables/python/marker/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    rendered = converter(source=source, output_dir=directory)
    text, _, images = text_from_rendered(rendered)

    return
