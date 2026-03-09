from pymupdf4llm_c import ExtractionError, to_json

import os
from pathlib import Path

import traceback
import orjson
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

library_name = "pymupdf4llm_c"

#@timer()
def extract_text_to_file_from_pdf_document (
                                                source_file: str
                                            ) -> str:
    """
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------
    directory = f"{source_file}.hwaifs/extractions/text/py/{library_name}/"
    Path(directory).mkdir(parents=True, exist_ok=True)
    
    try:
        output_file = f"{directory}/content.json"
        result_json = to_json(source_file, output=output_file)
        num_pages = 0

        # for path in json_files:
        #     with open(path, "r") as f:
        #         data = json.load(f)
        #         if "text" in data:
        #             result_txt = result_txt + data["text"] + "\n"

    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception reading text with {library_name} from PDF document source = {source_file} : {e}" \
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
        "num_pages" : num_pages,
        "time_start_1": time_start_1,
        "time_end_1": time_stop_1,
        "time_total_1": time_total_1,
        "pages_per_second_1" : num_pages / time_total_1,
        "time_start_2": time_start_2,
        "time_end_2": time_stop_2,
        "time_total_2": time_total_2,
        "pages_per_second_2" : num_pages / time_total_2,
        "time_start_3": time_start_3,
        "time_end_3": time_stop_3,
        "time_total_3": time_total_3,
        "pages_per_second_3" : num_pages / time_total_3
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.python.json", "w") as f:
        f.write(orjson.dumps(times, option=orjson.OPT_INDENT_2).decode())
   #---------------------------------------------------------------------------

    return result_json