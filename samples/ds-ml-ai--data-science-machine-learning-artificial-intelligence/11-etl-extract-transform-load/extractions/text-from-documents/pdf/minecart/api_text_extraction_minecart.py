import os
from pathlib import Path

def extract_text_to_file_from_pdf_document (source: str) -> str:
    pdf = open(f"{source}", 'rb')
    doc = minecart.Document(pdf)

    for page in doc.iter_pages():
        page.
    # for shape in page.shapes.iter_in_bbox((0, 0, 100, 200)):

    # im = page.images[0].as_pil()  # requires pillow
    # im.show()

    directory = f"{source}.hwaifs/text/python/minecart/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.md", "w") as f:
        f.write(result_md)

    return result_md
