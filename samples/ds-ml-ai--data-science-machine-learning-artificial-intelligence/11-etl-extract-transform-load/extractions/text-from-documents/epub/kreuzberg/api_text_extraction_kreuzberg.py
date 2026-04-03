from kreuzberg import extract_file_sync

import os
from pathlib import Path

import traceback
import orjson
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

library_name = "kreuzberg"

#@timer()
def extract_text_to_file_from_epub_document (
                                                source_file: str
                                            ) -> str:

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------
    directory = f"{source_file}.hwaifs/extractions/text/py/{library_name}/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    try:
        result = extract_file_sync(source_file)
        result_txt = result.content

        # num_pages = result.num_pages  # or result.page_count, result.pages, etc.
        
        if "pdf" in result.metadata:
            pdf_meta = result.metadata["epub"]
            num_pages = pdf_meta.get('page_count')
        
    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception reading text with {library_name} from EPUB document source = {source_file} : {e}" \
            + \
            tb
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)
        
        return

    # save to file
    with open(f"{directory}/content.txt", "w") as f:
        f.write(result_txt) 

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
        "num_pages" : num_pages,
        "pages_per_second_1" : num_pages / time_total_1,
        "pages_per_second_2" : num_pages / time_total_2,
        "pages_per_second_3" : num_pages / time_total_3,
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.py.json", "w") as f:
        f.write(orjson.dumps(times, option=orjson.OPT_INDENT_2).decode())
    #---------------------------------------------------------------------------

    return result_txt
