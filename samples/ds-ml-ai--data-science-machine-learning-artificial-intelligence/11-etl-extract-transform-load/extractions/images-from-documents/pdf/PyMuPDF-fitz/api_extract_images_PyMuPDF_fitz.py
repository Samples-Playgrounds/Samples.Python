import fitz as mu  # PyMuPDF
from pathlib import Path


def extract_images_from_pdf (source: str) -> str:

    directory = f"{source}.hwaifs/images/python/PyMuPDF-fitz/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    with mu.open(source) as pdf:
        for page in pdf:
            for info in page.get_images(full=True):
                xref = info[0]
                img = pdf.extract_image(xref)

                ext, data = img['ext'], img['image']

                with open(f'{directory}/{xref}.{ext}', 'wb') as f:
                    f.write(data)