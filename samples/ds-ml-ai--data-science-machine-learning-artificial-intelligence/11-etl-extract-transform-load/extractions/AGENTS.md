# ETL Text Extraction Repository

Python implementations for extracting text from documents, images, audio, and video for benchmarking.

## Build & Test Commands

### Run All Extractors
```bash
./test.sh                    # From extractions/ root
```

### Run Single Extractor
```bash
cd text-from-documents/pdf/<extractor-name>
./test.sh                    # Auto-setup venv + run
```

### Manual Execution
```bash
cd <extractor-directory>
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Code Style Guidelines

### File Organization
- `main.py` - Entry point, iterates over source documents
- `api_*.py` - Extraction logic and utility functions
- `test.sh` - Venv setup + execution script
- `requirements.txt` - Dependencies (generated via `pip freeze`)

### Naming Conventions
- Functions: `snake_case` with descriptive prefixes
  - `extract_text_to_file_from_pdf_document(source: str) -> str`
- Variables: `snake_case`
- Files: lowercase with hyphens/underscores
- Classes: `PascalCase`

### Type Hints
Always include type hints:
```python
def extract_text(source: str) -> str:
    """Extract text from document."""
```

### Import Order
```python
# 1. Standard library
import json
import os
import time
import traceback
from pathlib import Path
from time import perf_counter

# 2. Third-party
import doctr
import orjson
```

### Error Handling
Log exceptions to timestamped JSON:
```python
try:
    result = extract(source)
except Exception as e:
    tb = traceback.format_exc()
    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    Path(directory).mkdir(parents=True, exist_ok=True)
    with open(f"{directory}/exception-{timestamp}.json", "w") as f:
        f.write(f"Exception: {e}\n{tb}")
```

### Performance Timing
Use three timing methods:
```python
time_start_1 = time.time()
time_start_2 = perf_counter()
time_start_3 = perf_counter_ns()

# ... operation ...

time_total_1 = time.time() - time_start_1
time_total_2 = perf_counter() - time_start_2
time_total_3 = (perf_counter_ns() - time_start_3) / 1_000_000_000
```

### Output Structure
```
{source}.hwaifs/text/py/<extractor-name>/
├── content.txt           # Extracted text
├── content.md            # Extracted markdown
├── content.json          # JSON data
├── exception-*.json      # Exception logs
└── performance-data-*.json  # Benchmarks
```

### JSON Output Pattern
```python
output = {"result": data, "metadata": info, "time_total": elapsed}
Path(directory).mkdir(parents=True, exist_ok=True)
with open(f"{directory}/output.json", "w") as f:
    json.dump(output, f, indent=4)
```

## Project Structure

```
extractions/
├── AGENTS.md              # This file
├── test.sh                # Root test runner
├── list.md                # Extraction types
├── text-from-documents/   # PDF, EPUB, HTML, DOCX, XLSX, PPTX
├── text-from-images/      # OCR-based extraction
├── text-from-audio/       # Speech recognition
├── audio-from-video/      # Audio track extraction
├── tables-from-images/    # Table detection/extraction
├── summarizations/        # LLM-based summarization
└── structured-info/       # Structured data extraction
```

## Quick Reference

| Task | Command |
|------|---------|
| Run all | `./test.sh` |
| Single extractor | `cd <dir> && ./test.sh` |
| Manual run | `cd <dir> && source .venv/bin/activate && python main.py` |
| Setup venv | `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` |

## Notes

- Each extractor has isolated virtual environment
- Source documents defined in `data.py` (parent directory)
- Timestamps use ISO format (colons replaced with hyphens)
- No Cursor rules or Copilot instructions found