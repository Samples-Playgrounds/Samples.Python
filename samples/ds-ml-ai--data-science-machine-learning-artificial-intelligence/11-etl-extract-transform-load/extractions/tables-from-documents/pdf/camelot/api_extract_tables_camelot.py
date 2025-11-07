import camelot
import json
from pathlib import Path


def extract_tables_to_files_from_pdf_document (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/tables/python/camelot/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    tables = camelot.read_pdf(source)

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

    return

