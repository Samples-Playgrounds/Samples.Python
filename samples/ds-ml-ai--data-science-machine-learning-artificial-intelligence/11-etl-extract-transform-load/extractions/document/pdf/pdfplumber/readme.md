# pdfplumber

*   https://github.com/jsvine/pdfplumber

*   https://www.pdfplumber.com/


```shell
pip install pdfplumber
```

```python
import pdfplumber

with pdfplumber.open("path/to/file.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page.chars[0])
```
   