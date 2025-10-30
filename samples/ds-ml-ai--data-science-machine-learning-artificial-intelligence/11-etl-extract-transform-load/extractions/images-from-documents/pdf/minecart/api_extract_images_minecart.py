import minecart


def extract_tables_to_files (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/images/python/pikepdf/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    pdffile = open(source, 'rb')
    doc = minecart.Document(pdffile)

    page_no = 1
    for page in doc.iter_pages():
        img_no = 1
        for i in range(len(page.images)):
            try:
                im = page.images[i].as_pil()  # requires pillow
                count = count + 1
                im.save(f"{directory}/img-{count}.jpg")
            except:
                print('Error encountered at %s' % filename)
            img_no += 1

    page_no += 1
