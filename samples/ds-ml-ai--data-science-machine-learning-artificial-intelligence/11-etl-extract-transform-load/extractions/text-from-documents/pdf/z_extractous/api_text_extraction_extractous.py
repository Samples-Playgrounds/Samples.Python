from extractous import Extractor

import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def extract_text_to_file_from_any_document (source: str) -> str:

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------


    # Create a new extractor
    extractor = Extractor()
    extractor = extractor.set_extract_string_max_length(1000)
    
    # if you need an xml
    # extractor = extractor.set_xml_output(True)

    # Extract text from a file
    print(result)
    print(metadata)

    directory = f"{source}.hwaifs/text/py/extractous/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    reader, metadata = extractor.extract_file(source)

    result_txt = ""
    buffer = reader.read(4096)
    while len(buffer) > 0:
        result_txt += buffer.decode("utf-8")
        buffer = reader.read(4096)

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
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.python.json", "w") as f:
        f.write(json.dumps(times, indent=4))
    #---------------------------------------------------------------------------

    return result_txt
