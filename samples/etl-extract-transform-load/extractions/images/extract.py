import fitz as mu  # PyMuPDF

    with mu.open(filename) as pdf:
        for page in pdf:
            for info in page.getImageList():
                xref = info[0]
                img = pdf.extractImage(xref)

                ext, data = img['ext'], img['image']

                with open(f'{dirname}/{xref}.{ext}', 'wb') as f:
                    f.write(data)