from docling.document_converter import DocumentConverter


def extract_text_to_file_from_any_document (source: str) -> str:

    converter = DocumentConverter()
    result_doc = converter.convert(source)
    result_txt = result_doc.document.export_to_text()

    directory = f"{source}.hwaifs/text/python/docling/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.txt", "w") as f:
        f.write(result_txt) 

    return result_txt


def extract_markdown_to_file_from_any_document (source: str) -> str:

    converter = DocumentConverter()
    result_doc = converter.convert(source)
    result_md = result_doc.document.export_to_markdown()

    directory = f"{source}.hwaifs/text/python/docling/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.md", "w") as f:
        f.write(result_md)

    return result_md

from pathlib import Path
from docling.datamodel.document import InputDocument
from docling.datamodel.base_models import InputFormat
#from docling.document_backends.ms_word import MsWordDocumentBackend

from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.backend.msword_backend import MsWordDocumentBackend
from docling.backend.msexcel_backend import MsExcelDocumentBackend
from docling.document_converter import (
    DocumentConverter,
    PdfFormatOption,
    WordFormatOption,
    ExcelFormatOption
)
from docling.pipeline.simple_pipeline import SimplePipeline
from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline
from docling.datamodel.pipeline_options import PipelineOptions, EasyOcrOptions, TesseractOcrOptions
from docling.datamodel.base_models import ConversionStatus, InputFormat

def extract_markdown_to_file_from_any_document_complex (source: str) -> str:
    doc_converter = (
                DocumentConverter(  # all of the below is optional, has internal defaults.
                allowed_formats=[
                    InputFormat.PDF,
                    InputFormat.IMAGE,
                    InputFormat.DOCX,
                    InputFormat.HTML,
                    InputFormat.PPTX,
                    InputFormat.ASCIIDOC,
                    InputFormat.CSV,
                    InputFormat.MD,
                    InputFormat.XLSX
                ],  # whitelist formats, non-matching files are ignored.
                format_options={
                    InputFormat.PDF: PdfFormatOption(
                        pipeline_cls=StandardPdfPipeline, backend=PyPdfiumDocumentBackend
                    ),
                    InputFormat.DOCX: WordFormatOption(
                        pipeline_cls=SimplePipeline  , backend=MsWordDocumentBackend
                    ),
                    InputFormat.XLSX: ExcelFormatOption(
                        pipeline_cls=SimplePipeline  , backend=MsExcelDocumentBackend
                    ),
                },
            )
        )

    conv_results = doc_converter.convert_all([source])

    result_md = ""

    for res in conv_results:
        if res.document is None:
            print(f"Document {res.input.file.name} could not be converted.")
            continue
        result_md += res.document.export_to_markdown()
        
        # out_path = Path("allouts")
        # print(
        #     f"Document {res.input.file.name} converted."
        #     f"\nSaved markdown output to: {str(out_path)}"
        # )
        # _log.debug(res.document._export_to_indented_text(max_text_len=16))
        # # Export Docling document format to markdowndoc:
        #with (out_path / f"{res.input.file.stem}.md").open("w") as fp:
        #    fp.write(res.document.export_to_markdown())

    directory = f"{source}.hwaifs/text/python/docling/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}content.filetype-agnostic.md", "w") as f:
        f.write(result_md)

    return result_md