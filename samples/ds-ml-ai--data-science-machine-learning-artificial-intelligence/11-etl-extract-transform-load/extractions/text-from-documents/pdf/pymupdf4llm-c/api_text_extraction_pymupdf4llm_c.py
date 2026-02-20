from pymupdf4llm_c import ConversionConfig, ExtractionError, to_json

import os
from pathlib import Path

import traceback
import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def extract_text_to_file_from_pdf_document (source: str) -> str:

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/text/py/pymupdf4llm_c/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    result_txt = ""

    # save to file
    # with open(f"{directory}/content.txt", "w") as f:
    #     f.write(result_txt) 
    
    try:
        json_files = to_json(source, output_dir=directory)
    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception reading tables from PDF document source = {source} : {e}" \
            + \
            tb
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)
        
        return

    json_files = to_json(source, output_dir=directory)
    for path in json_files:
        with open(path, "r") as f:
            data = json.load(f)
            if "text" in data:
                result_txt = result_txt + data["text"] + "\n"

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
    with open(f"{directory}/performance-data-{timestamp}.python.json", "w") as f:
        f.write(json.dumps(times, indent=4))
    #---------------------------------------------------------------------------

    return result_txt