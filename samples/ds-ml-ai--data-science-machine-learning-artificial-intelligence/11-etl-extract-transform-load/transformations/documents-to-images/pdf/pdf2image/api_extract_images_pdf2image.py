from pdf2image import convert_from_path
from pathlib import Path


def extract_tables_to_files (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/images/python/pdf2image/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    pages = convert_from_path(source, 500)

    for count, page in enumerate(pages):
        page.save(f"{directory}/p{count}.jpg", 'JPEG')
