from docling.document_converter import DocumentConverter
import pandas as pd
import json
from pathlib import Path
 
def extract_tables_to_files_from_pdf_document (source: str) -> str:
    """
    """
    directory = f"{source}.hwaifs/tables/python/docling/"
    Path(directory).mkdir(parents=True, exist_ok=True)

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
