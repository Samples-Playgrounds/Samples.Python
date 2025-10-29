from pikepdf import Pdf, PdfImage
from pathlib import Path


def extract_images_from_pdf (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/images/python/pikepdf/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    example = Pdf.open(source)

    for i, page in enumerate(example.pages):
        for j, (name, raw_image) in enumerate(page.images.items()):
            image = PdfImage(raw_image)
            out = image.extract_to(fileprefix=f"{directory}/img-page{i:03}-img{j:03}")


