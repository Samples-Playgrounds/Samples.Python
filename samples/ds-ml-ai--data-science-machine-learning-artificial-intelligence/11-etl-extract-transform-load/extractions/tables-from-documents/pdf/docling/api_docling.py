import pandas as pd
from docling.document_converter import DocumentConverter
 
def extract_tables_to_files (source: str) -> str:
    """
    """
    doc_converter = DocumentConverter()

    conv_res = doc_converter.convert(source)

    # Iterate through tables
    # Export tables
    for table_ix, table in enumerate(conv_res.document.tables):
        table_df: pd.DataFrame = table.export_to_dataframe()

        # Save the table as MD
        print(f"## Table {table_ix}")
        print(table_df.to_markdown())

        doc_filename = source
        # Save the table as CSV
        element_csv_filename = f"{doc_filename}-table-{table_ix + 1}.csv"
        table_df.to_csv(element_csv_filename)

        element_excel_filename = f"{doc_filename}-table-{table_ix + 1}.xlsx"
        table_df.to_excel(element_excel_filename)

        # Save the table as HTML
        element_html_filename = f"{doc_filename}-table-{table_ix + 1}.html"
        # with element_html_filename.open("w") as fp:
        #     fp.write(table.export_to_html(doc=conv_res.document))
