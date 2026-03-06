# `mammoth`

*   https://pypi.org/project/mammoth/

*   https://github.com/mwilliamson/python-mammoth

```
pip install mammoth
```

```python
import mammoth

with open("document.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion

with open("document.docx", "rb") as docx_file:
    result = mammoth.extract_raw_text(docx_file)
    text = result.value # The raw text
    messages = result.messages # Any messages

```

*   https://github.com/mwilliamson/python-mammoth/blob/master/mammoth/conversion.py

*   https://github.com/ChatCRM/docx2md