# pdfminer.six

*   https://github.com/pdfminer/pdfminer.six

*   https://pypi.org/project/pdfminer.six/


```shell
pip install pdfminer.six
pip install 'pdfminer.six[image]'
```


```python
from pdfminer.high_level import extract_text

text = extract_text("example.pdf")
print(text)
```