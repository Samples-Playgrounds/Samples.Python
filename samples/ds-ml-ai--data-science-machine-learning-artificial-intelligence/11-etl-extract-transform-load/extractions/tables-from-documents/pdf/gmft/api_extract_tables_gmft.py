from gmft.auto import CroppedTable, TableDetector, AutoTableFormatter, AutoTableDetector
from gmft.pdf_bindings import PyPDFium2Document
import json
from pathlib import Path

detector = AutoTableDetector()
formatter = AutoTableFormatter()

def extract_tables_to_files_from_pdf_document(source: str): # produces list[CroppedTable]

    directory = f"{source}.hwaifs/tables/python/gmft/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    doc = PyPDFium2Document(source)
    tables = []
    for page in doc:
        tables += detector.extract(page)

    formatted_tables = [formatter.extract(table) for table in tables]

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

    return tables
