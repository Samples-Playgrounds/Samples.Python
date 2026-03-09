from doctr.io import DocumentFile
from doctr.models import ocr_predictor

import os
from pathlib import Path

import traceback
# import orjson # import error
import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

library_name = "docTR"

model = ocr_predictor(pretrained=True)


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

    result_txt = ""
    result_json = ""

    try:
        # PDF
        doc = DocumentFile.from_pdf(source_file)
        # Analyze
        result = model(doc)
        result_txt = result.render() 
        result_json = result.export()

        # NO direct way shown to get the number of pages
        num_pages = len(result.export()["pages"])

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

    # save to file
    with open(f"{directory}/content.txt", "w") as f:
        f.write(result_txt) 
    with open(f"{directory}/content.json", "w") as f:
        # f.write(orjson.dumps(times, option=orjson.OPT_INDENT_2).decode())
        f.write(json.dumps(result_json, indent=2))

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
    with open(f"{directory}/performance-data-{timestamp}.py.json", "w") as f:
        # f.write(orjson.dumps(times, option=orjson.OPT_INDENT_2).decode())
        f.write(json.dumps(times, indent=2))
    #---------------------------------------------------------------------------

    if result_txt is None and result_json is None:
        return "", ""

    if result_json is None and result_txt is not None:
        return result_txt, ""

    if result_txt is None and result_json is not None:
        return "", result_json

    return result_txt, result_json