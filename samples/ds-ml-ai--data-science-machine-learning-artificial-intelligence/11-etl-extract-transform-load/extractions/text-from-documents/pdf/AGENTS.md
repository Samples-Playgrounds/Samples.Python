# PDF Text Extraction Libraries Comparison

This repository contains multiple Python PDF text extraction library implementations for comparison and benchmarking.

---

## Build & Test Commands

### Run All Extractors (Root Level)
```bash
./test.sh
```

### Run Single Extractor
```bash
cd <extractor-directory>
./test.sh
```

### Manual Execution
```bash
cd <extractor-directory>
source .venv/bin/activate
python main.py
```

### Setup Virtual Environment
```bash
cd <extractor-directory>
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Run Single Test (Single Extractor)
```bash
cd <extractor-directory>
source .venv/bin/activate
python main.py
```

---

## Code Style Guidelines

### File Organization
- **Main script:** `main.py` - Entry point for extraction tasks
- **API module:** `api_*.py` - Extraction logic and utility functions
- **Test script:** `test.sh` - Virtual environment setup and execution
- **Dependencies:** `requirements.txt` - Generated via `pip freeze`

### Naming Conventions
- **Functions:** `snake_case` with descriptive prefixes (e.g., `extract_text_to_file_from_pdf_document`)
- **Variables:** `snake_case`
- **Files:** lowercase with hyphens or underscores
- **Classes:** `PascalCase`

### Type Hints
Always include type hints for function parameters and return types:
```python
def extract_text_to_file_from_pdf_document(source: str) -> str:
    """Extract text from PDF document."""
    pass
```

### Import Order
1. Standard library imports
2. Third-party imports

```python
import json
import os
import time
import traceback
from pathlib import Path
from time import perf_counter, perf_counter_ns

import doctr
```

### Error Handling
Exceptions are logged to timestamped JSON files in the output directory:
```python
import traceback
import datetime
from pathlib import Path

try:
    result = extract_pdf(source)
except Exception as e:
    tb = traceback.format_exc()
    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    directory = f"{source}.hwaifs/text/py/<extractor-name>/"
    Path(directory).mkdir(parents=True, exist_ok=True)
    with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
        f.write(f"Exception: {e}\n{tb}")
```

### Performance Timing
Use three timing methods for comprehensive benchmarking:
```python
import time
from time import perf_counter, perf_counter_ns

time_start_1 = time.time()
time_start_2 = perf_counter()
time_start_3 = perf_counter_ns()

# ... operation ...

time_stop_1 = time.time()
time_stop_2 = perf_counter()
time_stop_3 = perf_counter_ns()

time_total_1 = time_stop_1 - time_start_1
time_total_2 = time_stop_2 - time_start_2
time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000
```

### Output Directory Pattern
- Output files go to `{source}.hwaifs/text/py/<extractor-name>/`
- Directory is created automatically with `Path(...).mkdir(parents=True, exist_ok=True)`
- Files include:
  - `content.txt` - Extracted text
  - `content.md` - Extracted markdown
  - `content.json` - Extracted JSON data
  - `exception-*.json` - Exception logs
  - `performance-data-*.json` - Performance metrics

### JSON Output
```python
import json
from pathlib import Path

output = {
    "result": data,
    "metadata": info,
    "time_total": elapsed
}

Path(directory).mkdir(parents=True, exist_ok=True)
with open(f"{directory}/output.json", "w") as f:
    json.dump(output, f, indent=4)
```

### Documentation
Include setup instructions in module docstrings:
```python
"""
Extract text from PDF documents using <library-name>.

Setup:
    python -m venv .venv
    source .venv/bin/activate
    pip install <library-name>[optional-features]

Usage:
    python main.py
"""
```

---

## Project Structure

```
pdf/
├── AGENTS.md                    # This file
├── list.md                      # List of all extractors
├── test.sh                      # Root test runner (loops through all extractors)
├── <extractor-name>/
│   ├── main.py                  # Entry point, iterates over sources
│   ├── api_*.py                 # Extraction implementation
│   ├── test.sh                  # Setup venv + run main.py
│   ├── requirements.txt         # Dependencies (generated)
│   └── .hwaifs/                 # Output directory (generated)
│       └── text/
│           └── py/
│               └── <extractor-name>/
│                   ├── content.txt
│                   ├── content.md
│                   ├── content.json
│                   ├── exception-*.json
│                   └── performance-data-*.json
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Run all extractors | `./test.sh` (from pdf directory) |
| Run single extractor | `cd <dir> && ./test.sh` |
| Manual execution | `cd <dir> && source .venv/bin/activate && python main.py` |
| Setup venv | `cd <dir> && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` |

---

## Available Extractors

### Primary Extractors
- **docling** - Docling Document Converter
- **kreuzberg** - Kreuzberg PDF extractor
- **MarkItDown** - MarkItDown PDF converter
- **pdfminer.six** - PDF Miner library
- **pdfplumber** - PDF parsing library
- **PyMuPDF** - PyMuPDF (fitz)
- **pymupdf4llm** - PyMuPDF for LLM
- **pymupdf4llm-c** - PyMuPDF for LLM (C version)
- **PyPDF2** - PyPDF2
- **pdfium2** - PyPdfium2
- **unstructured** - Unstructured PDF partitioner

### OCR-based Extractors (Slower)
- **marker** - Marker PDF converter with OCR
- **pytesseract** - Tesseract OCR
- **docTR** - Document OCR

### Not Working / WIP
- z_pymupdf4llm-c
- z_deepdoctection-pytorch
- z_deepdoctection-tensorflow
- z_extractous
- z_multilingual-pdf2text
- z_pdf2text
- z_pypdf
- z_simple-pdf2text
- z_slate
- z_tika

---

## Notes

- Each extractor is isolated in its own virtual environment
- Tests compare extraction output, performance, and error handling
- Results are stored as JSON for comparison
- Exceptions include full traceback information
- All extractors use the same source documents from `data.py`
- Output directories are structured by extractor to enable easy comparison
- Performance timing uses three different methods for accuracy verification
- Timestamps in filenames use ISO format with colons replaced by hyphens