import pdfplumber
import pandas as pd

from pathlib import Path
import traceback

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

#@timer()
def extract_tables_to_files_from_pdf_document (source: str) -> str:
    """
    """

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/tables/py/pdfplumber/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    pdf = pdfplumber.open(source)
 
    # Iterate through each table found in the PDF
    for i, page in enumerate(pdf.pages):
        df = pd.DataFrame(pdf.pages[i].extract_table())

        element_md_filename = f"{directory}/p-t{i + 1 :05}.md"
        df.to_markdown(element_md_filename)

        element_csv_filename = f"{directory}/p-t{i + 1 :05}.csv"
        df.to_csv(element_csv_filename)

        element_excel_filename = f"{directory}/p-t{i + 1 :05}.xlsx"
        df.to_excel(element_excel_filename)

        element_html_filename = f"{directory}/p-t{i + 1 :05}.html"
        df.to_html(element_html_filename)

    #---------------------------------------------------------------------------
    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name" : "extract_tables_to_files_from_pdf_document",
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

    return

