# ETL Text Extraction Repository

This repository contains multiple Python implementations for extracting text from various document types, audio, images, and video for comparison and benchmarking.

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
extractions/
├── AGENTS.md                    # This file
├── list.md                      # List of all extraction types
├── test.sh                      # Root test runner (loops through all extractors)
├── text-from-documents/
│   ├── pdf/
│   │   ├── AGENTS.md            # PDF-specific guidelines
│   │   ├── list.md              # List of PDF extractors
│   │   ├── test.sh              # PDF test runner
│   │   └── <extractor-name>/
│   │       ├── main.py          # Entry point
│   │       ├── api_*.py         # Extraction implementation
│   │       ├── test.sh          # Setup venv + run main.py
│   │       ├── requirements.txt # Dependencies
│   │       └── .hwaifs/         # Output directory
│   ├── epub/
│   ├── html/
│   ├── rtf-rich-text-format/
│   ├── microsoft-excel-xlsx/
│   ├── microsoft-powerpoint-pptx/
│   └── ...
├── text-from-images/
├── text-from-audio/
├── audio-from-video/
├── code/
├── summarizations-synopsizations/
├── structured-information-from-text/
├── tables-from-documents/
├── tables-from-images/
└── images-from-documents/
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Run all extractors | `./test.sh` (from extractions directory) |
| Run single extractor | `cd <dir> && ./test.sh` |
| Manual execution | `cd <dir> && source .venv/bin/activate && python main.py` |
| Setup venv | `cd <dir> && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` |

---

## Available Extraction Types

### Text from Documents
- **PDF** - PDF text extraction libraries comparison
  - Primary: docling, kreuzberg, MarkItDown, pdfminer.six, pdfplumber, PyMuPDF, pymupdf4llm, PyPDF2, pdfium2, unstructured
  - OCR-based: marker, pytesseract, docTR
- **EPUB** - EPUB ebook text extraction
- **HTML** - HTML to text conversion
- **RTF** - Rich Text Format extraction
- **Microsoft Excel** - XLSX spreadsheet text extraction
- **Microsoft PowerPoint** - PPTX presentation text extraction

### Text from Images
- **OCR-based** - Text extraction from images using OCR
- **Table extraction** - Table detection and extraction from images

### Text from Audio
- **Speech recognition** - Audio to text conversion

### Audio from Video
- **Video to audio** - Extract audio tracks from video files
- **Audio processing** - Audio analysis and transcription

### Code
- **Code extraction** - Extract code from various formats

### Summarizations & Synopsizations
- **LLM-based** - Text summarization using LLMs
- **Extractive** - Extractive summarization techniques

### Structured Information from Text
- **LLM-based** - Extract structured data from unstructured text

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
- Cursor rules: None found
- Copilot rules: None found