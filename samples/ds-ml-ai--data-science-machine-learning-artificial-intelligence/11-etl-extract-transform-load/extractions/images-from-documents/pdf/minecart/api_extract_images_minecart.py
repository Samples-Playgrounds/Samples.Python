import minecart
from pathlib import Path
import traceback


def extract_tables_to_files (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/images/python/minecart/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    pdffile = open(source, 'rb')
    doc = minecart.Document(pdffile)

    page_no = 1
    for page in doc.iter_pages():
        img_no = 1
        for i in range(len(page.images)):
            try:
                im1 = page.images[i]
                im = im1.as_pil()  # requires pillow
                count = count + 1
                im.save(f"{directory}/img-p{page_no}-{count}.jpg")
            except Exception as e: 
                print(e)
                print('Error encountered at %s' % source)
                traceback.print_exc()

            img_no += 1

    page_no += 1
