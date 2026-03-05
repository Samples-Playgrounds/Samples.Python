import mistletoe

import json

import os
from pathlib import Path

import traceback
import datetime
import time
from time import perf_counter
from time import perf_counter_ns

def api_parse_analyze_markdown_mistletoe(source: str) -> str:
    """
    Parse markdown documents using mistletoe.

    Setup:
        python -m venv .venv
        source .venv/bin/activate
        pip install mistletoe

    Usage:
        python main.py
    """
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()

    directory = f"{source}.hwaifs/parse-analysis/py/mistletoe/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    try:
        with open(source, "r") as f:
            text = f.read()
        
        doc = mistletoe.Document(text)
        
        doc_dict = {
            "children": [str(child) for child in getattr(doc, 'children', [])],
            "line_number": getattr(doc, 'line_number', 0),
            "parent": str(type(doc.parent)) if hasattr(doc, 'parent') and doc.parent else None
        }
        txt_json_output = json.dumps(doc_dict, indent=4)
        
        html_output = mistletoe.markdown(text)
    except Exception as e:
        tb = traceback.format_exc()
        msg = f"Exception parsing markdown with mistletoe = {source} : {e}\n{tb}"
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)
        return ""

    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name": "api_parse_analyze_markdown_mistletoe",
        "time_start_1": time_start_1,
        "time_end_1": time_stop_1,
        "time_total_1": time_total_1,
        "time_start_2": time_start_2,
        "time_end_2": time_stop_2,
        "time_total_2": time_total_2,
        "time_start_3": time_start_3,
        "time_end_3": time_stop_3,
        "time_total_3": time_total_3,
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.py.json", "w") as f:
        f.write(json.dumps(times, indent=4))

    with open(f"{directory}/tokens.json", "w") as f:
        f.write(txt_json_output)
    
    with open(f"{directory}/content.html", "w") as f:
        f.write(html_output)

    with open(f"{directory}/content.md.json", "w") as f:
        f.write(txt_json_output)

    return txt_json_output