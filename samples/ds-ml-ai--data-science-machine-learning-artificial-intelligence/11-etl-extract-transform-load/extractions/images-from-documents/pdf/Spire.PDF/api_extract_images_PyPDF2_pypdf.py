from PyPDF2 import PdfReader
from pathlib import Path

        
def extract_images_from_pdf_to_files (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/images/python/PyPDF2-pypdf/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    reader = PdfReader(source)

    page_no = 1
    for page in reader.pages:
        img_no = 1
        images = []
        # https://pypdf2.readthedocs.io/en/3.0.0/modules/PageObject.html#PyPDF2._page.PageObject.images
        try:
            images.extend(page.images)
        except ValueError:
            images = []

        for image in images:
            name = image.name
            with open(f"{directory}/p{page_no}-{img_no}-{name}", "wb") as fp:
                fp.write(image.data)
            img_no += 1
        page_no += 1


