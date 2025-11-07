import tabula

import json
from pathlib import Path


def extract_tables_to_files_from_pdf_document (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/tables/python/tabula-py/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    dfs = tabula.read_pdf(source, pages='all')

    # Iterate through each table found in the PDF
    for i, df in enumerate(dfs):
        # Extract table data as a Pandas DataFrame, including headers
        # df = table.df                   # get a pandas DataFrame!
        # df.convert_into(
        #                 f"{source}", 
        #                 f"{directory}/table-{i}.camelot.csv",
        #                 output_format="csv",
        #                 pages='all'
        #                 )

        element_md_filename = f"{directory}/p-t{i + 1}.md"
        df.to_markdown(element_md_filename)

        element_csv_filename = f"{directory}/p-t{i + 1}.csv"
        df.to_csv(element_csv_filename)

        element_excel_filename = f"{directory}/p-t{i + 1}.xlsx"
        df.to_excel(element_excel_filename)

        element_html_filename = f"{directory}/p-t{i + 1}.html"
        df.to_html(element_html_filename)

    return
