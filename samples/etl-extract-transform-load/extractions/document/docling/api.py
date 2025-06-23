from docling.document_converter import DocumentConverter

def covert_pdf_file_to_text (source: str) -> str:
    converter = DocumentConverter()
    result_doc = converter.convert(source)
    result_txt = result_doc.document.export_to_text()

    return result_txt


def covert_pdf_file_to_markdown (source: str) -> str:
    converter = DocumentConverter()
    result_doc = converter.convert(source)
    result_txt = result_doc.document.export_to_markdown()

    return result_md

def covert_docx_file_to_markdown (source: str) -> str:

    in_path = Path(source)
    in_doc = InputDocument(
        path_or_stream=in_path,
        format=InputFormat.DOCX,
        backend=MsWordDocumentBackend,
    )
    backend = MsWordDocumentBackend(
        in_doc=in_doc,
        path_or_stream=in_path,
    )
    doc = backend.convert()
    doc