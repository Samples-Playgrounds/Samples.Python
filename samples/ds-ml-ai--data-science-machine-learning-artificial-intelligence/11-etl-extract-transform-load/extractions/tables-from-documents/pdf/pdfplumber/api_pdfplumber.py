import pdfplumber
import pandas as pd
 
def extract_tables_to_files (source: str) -> str:
    """
    """
    pdf = pdfplumber.open(source)
 
    # Iterate through each table found in the PDF
    for i, page in enumerate(pdf.pages):
        print(f"page {i}")
        df = pd.DataFrame(pdf.pages[i].extract_table())
        df_total.concat(df)
        df.to_csv(f"{source}.page-{i}.tables.pdfplumber.csv")      # to_json, to_excel, to_html
        df.to_json(f"{source}.page-{i}.tables.pdfplumber.json")    # to_json, to_excel, to_html
        # df.to_excel(f"{source}.page-{i}.tables.pdfplumber.xlsx")   # to_json, to_excel, to_html
        df.to_html(f"{source}.page-{i}.tables.pdfplumber.html")    # to_json, to_excel, to_html
