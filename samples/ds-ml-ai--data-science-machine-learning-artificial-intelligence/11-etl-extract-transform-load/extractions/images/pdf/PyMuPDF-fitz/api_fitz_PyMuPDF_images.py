import fitz as mu  # PyMuPDF

def extract_images_from_pdf (filename: str) -> str:

    folder = f'{filename}.images'
    mu.os.makedirs(folder, exist_ok=True)

    with mu.open(filename) as pdf:
        for page in pdf:
            for info in page.get_images(full=True):
                xref = info[0]
                img = pdf.extract_image(xref)

                ext, data = img['ext'], img['image']

                with open(f'{folder}/{xref}.{ext}', 'wb') as f:
                    f.write(data)