

```python
from ollama import chat
from ollama import ChatResponse

files = [
    f"/Users/Shared/Projects/e/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf",
]


prompt = """
Extract data from text:
{text}
"""

response: ChatResponse = chat(model='gemma3:27b', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
```

```
.hwaifs/
├── images
│   └── python
│       ├── PyMuPDF-fitz
│       ├── PyPDF2-pypdf
│       ├── minecart
│       └── pikepdf
├── tables
│   └── python
│       ├── gmft
│       ├── pdfplumber
│       └── tabula-py
└── text
    └── python
        ├── PyMuPDF_fitz
        ├── PyPDF2
        ├── docling
        ├── marker
        ├── markitdown
        ├── pdf2text
        ├── pdfminer_six
        ├── pdfplumber
        ├── pymupdf4llm
        ├── pymupdf4llm_c
        ├── pypdfium2
        ├── pytesseract
        └── unstructured
```