from pdfminer.high_level import extract_text
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage

import os
from pathlib import Path

import traceback
import orjson
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def extract_text_to_file_from_pdf_document (source: str) -> str:
    """
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    try:
        pages = list(extract_pages(source))
        num_pages = len(pages)
        result_txt_high_level = extract_text(source)  
              
        with open(source, 'rb') as fp:
            parser = PDFParser(fp)
            doc = PDFDocument(parser)
            num_pages = len(list(PDFPage.create_pages(doc)))
            # pages = resolve1(doc.catalog['Pages'])
            # pages_count = pages.get('Count', 0)

        directory = f"{source}.hwaifs/extractions/text/py/pdfminer_six/"
        Path(directory).mkdir(parents=True, exist_ok=True)

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
        f.write(orjson.dumps(times, option=orjson.OPT_INDENT_2).decode())
    #---------------------------------------------------------------------------

    return result_txt

