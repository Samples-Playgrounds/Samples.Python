from gmft.auto import CroppedTable, TableDetector, AutoTableFormatter, AutoTableDetector
from gmft.pdf_bindings import PyPDFium2Document

from pathlib import Path
import traceback

import orjson
import datetime
import time
from time import perf_counter
from time import perf_counter_ns
# from timer import timer

library_name = "gmft"

detector = AutoTableDetector()
formatter = AutoTableFormatter()

#@timer()
def extract_tables_to_files_from_pdf_document(
                                                source_file: str
                                            ):
    # produces list[CroppedTable]
    """
    """

    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------
    directory = f"{source_file}.hwaifs/extractions/tables/py/{library_name}/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    try:
        doc = PyPDFium2Document(source_file)
        num_pages = len(doc)
        tables = []
        for page in doc:
            tables += detector.extract(page)

        formatted_tables = [formatter.extract(table) for table in tables]
    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception reading tables with {library_name} from PDF document source = {source_file} : {e}" \
            + \
            tb
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)
        
        return

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
        "num_pages" : num_pages,
        "pages_per_second_1" : num_pages / time_total_1,
        "pages_per_second_2" : num_pages / time_total_2,
        "pages_per_second_3" : num_pages / time_total_3,
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.py.json", "w") as f:
        f.write(orjson.dumps(times, option=orjson.OPT_INDENT_2).decode())
    #---------------------------------------------------------------------------

    return tables
