# Translations

readme.md

*   https://www.geeksforgeeks.org/how-to-extract-images-from-pdf-in-python/

    ```shell
    pip install PyMuPDF Pillow
    ```

*   https://pypdf.readthedocs.io/en/stable/user/extract-images.html

*   https://medium.com/@alexaae9/python-how-to-extract-images-from-pdf-documents-9492a767a613

*   https://github.com/gsmatheus/pdf-image-extractor

*   https://karthikeyanrathinam.medium.com/extracting-text-and-images-from-pdfs-using-python-a-step-by-step-guide-b9c8506fd613

*   https://thepythoncode.com/article/extract-pdf-images-in-python

*   Extract text, links, images, tables from Pdf with Python | PyMuPDF, PyPdf, PdfPlumber tutorial

    *   https://www.youtube.com/watch?v=G0PApj7YPBo

*   https://gist.github.com/delannoy/0db41032713f1256e63ab619c0a0f19d

*   https://aliarefwriorr.medium.com/extract-all-images-from-pdf-in-python-cda3dc195abd

*   https://pypdf2.readthedocs.io/en/3.0.0/user/extract-images.html

*   https://www.reddit.com/r/Python/comments/ldgszd/extracting_images_from_pdfs/

```python
# extract.py
import fitz as mu  # PyMuPDF
import os
import sys


for filename in sys.argv[1:]:
    dirname, _ = os.path.splitext(filename)
    os.makedirs(dirname, exist_ok=True)

    with mu.open(filename) as pdf:
        for page in pdf:
            for info in page.getImageList():
                xref = info[0]
                img = pdf.extractImage(xref)

                ext, data = img['ext'], img['image']

                with open(f'{dirname}/{xref}.{ext}', 'wb') as f:
                    f.write(data)
```

```shell
```