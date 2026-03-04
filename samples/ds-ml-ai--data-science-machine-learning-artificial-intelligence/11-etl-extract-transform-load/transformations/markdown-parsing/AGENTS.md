# Markdown Parsing Libraries Comparison

This repository contains multiple Python markdown parsing library implementations for comparison and benchmarking.

---

## Build & Test Commands

### Run All Parsers (Root Level)
```bash
./test.sh
```

### Run Single Parser
```bash
cd <parser-directory>
./test.sh
```

### Manual Execution
```bash
cd <parser-directory>
source .venv/bin/activate
python main.py
```

### Setup Virtual Environment
```bash
cd <parser-directory>
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Code Style Guidelines

### File Organization
- **Main script:** `main.py` - Entry point for parsing tasks
- **API module:** `api_*.py` - Parsing logic and utility functions
- **Test script:** `test.sh` - Virtual environment setup and execution
- **Dependencies:** `requirements.txt` - Generated via `pip freeze`

### Naming Conventions
- **Functions:** `snake_case` with descriptive prefixes (e.g., `api_parse_analyze_markdown_markdown_it_py`)
- **Variables:** `snake_case`
- **Files:** lowercase with hyphens or underscores

### Type Hints
Always include type hints for function parameters and return types:
```python
def api_parse_analyze_markdown_markdown_it_py(source: str) -> str:
    """Parse markdown and return tokens."""
    pass
```

### Import Order
1. Standard library imports
2. Third-party imports

```python
import json
import os
import time
from pathlib import Path

import markdown_it
```

### Error Handling
Exceptions are logged to timestamped JSON files in the output directory:
```python
import traceback
import datetime
from pathlib import Path

try:
    result = parse_markdown(source)
except Exception as e:
    tb = traceback.format_exc()
    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    directory = f"{source}.hwaifs/parse-analysis/py/markdown-it-py/"
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

times = {
    "time_total_1": time_stop_1 - time_start_1,
    "time_total_2": time_stop_2 - time_start_2,
    "time_total_3": (time_stop_3 - time_start_3) / 1_000_000_000,
}
```

### Output Directory Pattern
- Output files go to `{source}.hwaifs/parse-analysis/py/<parser-name>/`
- Directory is created automatically with `Path(...).mkdir(parents=True, exist_ok=True)`
- Files include: `tokens.json`, `content.html`, `exception-*.json`, `performance-data-*.json`

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
Parse markdown documents using markdown-it-py.

Setup:
    python -m venv .venv
    source .venv/bin/activate
    pip install markdown-it-py[plugins]

Usage:
    python main.py
"""
```

---

## Project Structure

```
markdown-parsing/
├── AGENTS.md              # This file
├── README.md
├── test.sh                # Root test runner (loops through all parsers)
├── data.py                # Shared data definitions (files_documents_pdfs)
├── <parser-name>/
│   ├── main.py            # Entry point, iterates over sources
│   ├── api_*.py           # Parsing implementation
│   ├── test.sh            # Setup venv + run main.py
│   ├── requirements.txt   # Dependencies (generated)
│   └── .hwaifs/           # Output directory (generated)
│       └── parse-analysis/
│           └── py/
│               └── <parser-name>/
│                   ├── tokens.json
│                   ├── content.html
│                   ├── exception-*.json
│                   └── performance-data-*.json
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Run all parsers | `./test.sh` (from root) |
| Run single parser | `cd <dir> && ./test.sh` |
| Manual execution | `cd <dir> && source .venv/bin/activate && python main.py` |
| Setup venv | `cd <dir> && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` |

---

## Notes

- Each parser is isolated in its own virtual environment
- Tests compare parsing output, performance, and error handling
- Results are stored as JSON for comparison
- Exceptions include full traceback information
- All parsers use the same source documents from `data.py`
- Output directories are structured by parser to enable easy comparison