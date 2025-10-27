# Image Extraction

readme.md

*   https://www.geeksforgeeks.org/how-to-extract-images-from-pdf-in-python/

    ```shell
    pip install PyMuPDF Pillow
    ```

    *   https://www.geeksforgeeks.org/python/how-to-extract-images-from-pdf-in-python/


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

*   https://github.com/gsmatheus/pdf-image-extractor/blob/main/main.py

    ```shell
    pip install pdfplumber pymupdf pillow
    ```

*   https://pypdf.readthedocs.io/en/latest/user/extract-images.html

    ```
    pip install pypdf
    ```
    
*   https://medium.com/@alice.yang_10652/extract-images-and-image-information-from-pdf-with-python-10719a3bda81

*   https://medium.com/@alexaae9/python-how-to-extract-images-from-pdf-documents-9492a767a613

*   https://gist.github.com/delannoy/0db41032713f1256e63ab619c0a0f19d

*   https://python.plainenglish.io/python-libraries-for-extracting-images-from-pdfs-6394d85b5135

*   https://thepythoncode.com/article/extract-pdf-images-in-python

*   https://mybyways.com/blog/extracting-images-from-pdf-files

*   https://www.reddit.com/r/Python/comments/ldgszd/extracting_images_from_pdfs/

*   https://geekflare.com/dev/extract-text-links-images-from-pdf-using-python/

*   https://geekflare.com/dev/extract-text-links-images-from-pdf-using-python/

*   https://www.geeksforgeeks.org/python/working-with-pdf-files-in-python/

*   https://dev.to/cloudytech147/a-step-by-step-guide-to-extract-images-from-pdf-in-python-3gip

*   https://python.plainenglish.io/extracting-images-from-a-pdf-using-python-45bbb3f41e51

*   https://levelup.gitconnected.com/extract-images-from-pdf-using-python-97e2ad31c7f1

*   https://celeryq.org/extract-images-from-pdf-python/
