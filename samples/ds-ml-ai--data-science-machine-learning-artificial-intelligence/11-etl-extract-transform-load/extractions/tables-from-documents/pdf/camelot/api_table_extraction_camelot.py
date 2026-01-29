import camelot

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

    directory = f"{source}.hwaifs/tables/py/camelot/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    try:
        tables = camelot.read_pdf(source)
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

    tables.export(f'{directory}/tables.csv', f='csv', compress=False) # json, excel, html
    tables.export(f'{directory}/tables.json', f='json', compress=False) # json, excel, html

    # Iterate through each table found in the PDF
    for i, table in enumerate(tables):
        # Extract table data as a Pandas df, including headers
        df = table.df                   # get a pandas df!
        df.to_csv(f"{directory}/df.tables-{i}.csv")      # to_json, to_excel, to_html
        df.to_json(f"{directory}/df.tables-{i}.json")    # to_json, to_excel, to_html
        df.to_excel(f"{directory}/df.tables-{i}.xlsx")   # to_json, to_excel, to_html
        df.to_html(f"{directory}/df.tables-{i}.html")    # to_json, to_excel, to_html

        pr = table.parsing_report
        with open(f"{directory}/df.tables-{i}.parsing_report.json", "w") as f:
            f.write(json.dumps(pr))

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

