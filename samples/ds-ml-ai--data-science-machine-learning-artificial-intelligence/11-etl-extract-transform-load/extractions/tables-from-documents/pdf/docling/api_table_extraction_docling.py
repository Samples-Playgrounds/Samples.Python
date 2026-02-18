from docling.document_converter import DocumentConverter
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

    directory = f"{source}.hwaifs/tables/py/docling/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    try:
        doc_converter = DocumentConverter()

        conv_res = doc_converter.convert(source)

        # Iterate through tables
        # Export tables
        for table_ix, table in enumerate(conv_res.document.tables):
            df: pd.DataFrame = table.export_to_dataframe(doc_converter)

            element_md_filename = f"{directory}/p-t{table_ix + 1}.md"
            df.to_markdown(element_md_filename)

            element_csv_filename = f"{directory}/p-t{table_ix + 1}.csv"
            df.to_csv(element_csv_filename)

            element_excel_filename = f"{directory}/p-t{table_ix + 1}.xlsx"
            df.to_excel(element_excel_filename)

            element_html_filename = f"{directory}/  p-t{table_ix + 1}.html"
            df.to_html(element_html_filename)
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

