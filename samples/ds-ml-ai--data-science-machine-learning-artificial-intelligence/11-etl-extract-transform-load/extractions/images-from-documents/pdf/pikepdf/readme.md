# `pikepdf`

*   https://github.com/pikepdf/pikepdf

*   https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python

```python
from pikepdf import Pdf, PdfImage

filename = "sample-in.pdf"
example = Pdf.open(filename)

for i, page in enumerate(example.pages):
    for j, (name, raw_image) in enumerate(page.images.items()):
        image = PdfImage(raw_image)
        out = image.extract_to(fileprefix=f"{filename}-page{i:03}-img{j:03}")
```