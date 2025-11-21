# `pymupdf4llm-c`

readme,md

TODO

*   https://github.com/intercepted16/pymupdf4llm-C

*   https://pypi.org/project/pymupdf4llm-c/

```
pip install pymupdf4llm-c 
```

```python
from pathlib import Path

from pymupdf4llm_c import ConversionConfig, ExtractionError, to_json

pdf_path = Path("example.pdf")
output_dir = pdf_path.with_name(f"{pdf_path.stem}_json")

try:
    json_files = to_json(pdf_path, output_dir=output_dir)
    print(f"Generated {len(json_files)} files:")
    for path in json_files:
        print(f"  - {path}")
except ExtractionError as exc:
    print(f"Extraction failed: {exc}")
```

*   