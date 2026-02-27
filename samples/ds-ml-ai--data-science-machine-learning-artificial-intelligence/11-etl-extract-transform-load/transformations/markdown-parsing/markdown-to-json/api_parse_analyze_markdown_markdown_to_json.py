import markdown_to_json

import traceback
import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

def api_parse_analyze_markdown_markdown_to_json (source: str) -> str:
    """
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/parse-analysis/py/markdown-to-json/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    try:
        with open(source, 'r') as f:
            text = f.read()

        dictified = markdown_to_json.dictify(text)
        jsonified = markdown_to_json.jsonify(text)

        with open(f"{directory}/dictified.json", "w") as f:
            f.write(json.dumps(dictified))
        with open(f"{directory}/jsonified.json", "w") as f:
            f.write(jsonified)
        
    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception parsing markdown with markdown-it-py = {source} : {e}" \
            + \
            tb
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)
        
        return

    #---------------------------------------------------------------------------
    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name" : "extract_text_to_file_from_any_document",
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
    #---------------------------------------------------------------------------

    return jsonified
