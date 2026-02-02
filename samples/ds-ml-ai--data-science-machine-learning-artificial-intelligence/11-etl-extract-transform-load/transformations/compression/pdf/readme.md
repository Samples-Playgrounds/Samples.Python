# Compresion PDF

*   size reduction for transfer (mail communication, upload/download)

*   PyPDF2 

    https://pypdf2.readthedocs.io/en/3.x/

    https://pypdf.readthedocs.io/en/stable/user/file-size.html


```python
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

ruta = Path("pypdf_1/pesado.pdf")
reader = PdfReader(ruta)
writer = PdfWriter()

for page in reader.pages:
    page.compress_content_streams()  # Esto consume mucha CPU!
    level=9
    writer.add_page(page)

with open("pypdf_1/out.pdf", "wb") as f:
    writer.write(f)
```

https://stackoverflow.com/questions/76297824/pypdf2-unable-to-compress-pdf

https://stackoverflow.com/questions/10326836/compress-pdfs-using-python

https://www.reddit.com/r/learnprogramming/comments/1bew411/trying_to_make_python_code_to_reduce_pdf_file_size/

