from gmft.auto import CroppedTable, TableDetector, AutoTableFormatter, AutoTableDetector
from gmft.pdf_bindings import PyPDFium2Document

detector = AutoTableDetector()
formatter = AutoTableFormatter()

def ingest_pdf(pdf_path): # produces list[CroppedTable]
    doc = PyPDFium2Document(pdf_path)
    tables = []
    for page in doc:
        tables += detector.extract(page)
    return tables, doc
