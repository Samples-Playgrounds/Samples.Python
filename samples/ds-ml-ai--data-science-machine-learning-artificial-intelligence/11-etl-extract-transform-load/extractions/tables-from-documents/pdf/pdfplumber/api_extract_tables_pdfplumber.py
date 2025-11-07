import pdfplumber
import pandas as pd

import json
from pathlib import Path

def extract_tables_to_files_from_pdf_document (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/tables/python/pdfplumber/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    pdf = pdfplumber.open(source)
 
    # Iterate through each table found in the PDF
    for i, page in enumerate(pdf.pages):
        df = pd.DataFrame(pdf.pages[i].extract_table())

        element_md_filename = f"{directory}/p-t{i + 1}.md"
        df.to_markdown(element_md_filename)

        element_csv_filename = f"{directory}/p-t{i + 1}.csv"
        df.to_csv(element_csv_filename)

        element_excel_filename = f"{directory}/p-t{i + 1}.xlsx"
        df.to_excel(element_excel_filename)

        element_html_filename = f"{directory}/p-t{i + 1}.html"
        df.to_html(element_html_filename)

    return

