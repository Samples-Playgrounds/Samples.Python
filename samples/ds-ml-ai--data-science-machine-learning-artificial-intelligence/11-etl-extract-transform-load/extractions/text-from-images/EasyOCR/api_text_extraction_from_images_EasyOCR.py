import easyocr

import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def extract_text_to_file_from_image (
                                        source: str,
                                        languages: list = ['en', 'hr', 'de']
                                    ) -> str:

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/text/py/EasyOCR/"
    Path(directory).mkdir(parents=True, exist_ok=True)


    result_txt = ""

    try:
        # https://www.jaided.ai/easyocr/modelhub/

        # this needs to run only once to load the model into memory
        reader = easyocr.Reader(languages) 
        result = reader.readtext(source)
    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception extracting images from PDF document source = {source} : {e}" \
            + \
            tb
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)
        
        return

    for (bbox, text, prob) in result:
        result_txt += text + '\n'

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
        "function_method_name" : "extract_text_to_file_from_image",
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

    return result_txt

