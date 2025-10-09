import camelot
import json


def extract_tables_to_files (source: str) -> str:
    """
    """
    tables = camelot.read_pdf(source)

    tables.export(f'{source}.csv', f='csv', compress=True) # json, excel, html

    # Iterate through each table found in the PDF
    for i, table in enumerate(tables):
        # Extract table data as a Pandas DataFrame, including headers
        df = table.df                   # get a pandas DataFrame!
        df.to_csv(f"{source}.page-.{i}.tables.camelot.csv")      # to_json, to_excel, to_html
        df.to_json(f"{source}.page-.{i}.tables.camelot.json")    # to_json, to_excel, to_html
        df.to_excel(f"{source}.page-.{i}.tables.camelot.xlsx")   # to_json, to_excel, to_html
        df.to_html(f"{source}.page-.{i}.tables.camelot.html")    # to_json, to_excel, to_html

        pr = table.parsing_report
        with open(f"{source}.parsing_report.json", "w") as f:
            f.write(json.dumps(pr)
) 

