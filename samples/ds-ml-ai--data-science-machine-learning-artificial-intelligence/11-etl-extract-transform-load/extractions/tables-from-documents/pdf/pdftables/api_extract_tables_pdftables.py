import pdftables

import json
from pathlib import Path


def extract_tables_to_files_from_pdf_document (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/tables/python/pdftables/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    with open(source, 'rb') as fh:
        tables = pdftables.get_tables(fh)


    # Iterate through each table found in the PDF
    for i, table in enumerate(tables):
        # Extract table data as a Pandas DataFrame, including headers
        df = table.df                   # get a pandas DataFrame!
        df.to_csv(f"{source}.tables-{i}.pdftables.csv")      # to_json, to_excel, to_html
        df.to_json(f"{source}.tables-{i}.pdftables.json")    # to_json, to_excel, to_html
        df.to_excel(f"{source}.tables-{i}.pdftables.xlsx")   # to_json, to_excel, to_html
        df.to_html(f"{source}.tables-{i}.pdftables.html")    # to_json, to_excel, to_html


