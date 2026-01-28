from gmft.auto import CroppedTable, TableDetector, AutoTableFormatter, AutoTableDetector
from gmft.pdf_bindings import PyPDFium2Document

from pathlib import Path
import traceback

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer


detector = AutoTableDetector()
formatter = AutoTableFormatter()

#@timer()
def extract_tables_to_files_from_pdf_document(source: str): # produces list[CroppedTable]
    """
    """

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/tables/py/gmft/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    doc = PyPDFium2Document(source)
    tables = []
    for page in doc:
        tables += detector.extract(page)

    formatted_tables = [formatter.extract(table) for table in tables]

    for i, table in enumerate(formatted_tables):
        try:
            df = table.df()
            df.to_markdown(f"{directory}/df.tables-{i}.md")
            df.to_csv(f"{directory}/df.tables-{i}.csv")
            df.to_excel(f"{directory}/df.tables-{i}.xlsx")
            df.to_html(f"{directory}/df.tables-{i}.html")
            #df.to_json(f"{directory}/df.tables-{i}.json")
        except Exception as e:
            msg = f"Error saving table {i}: {e}"
            print(msg)
            with open(f"{directory}/df.tables-{i}.md", "w") as f:
                f.write(msg)

    doc.close() # once you're done with the document

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

    return tables
