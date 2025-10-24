from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

def covert_pdf_file_to_markdown (source: str) -> str:
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )
    rendered = converter(source)
    result_md, _, images = text_from_rendered(rendered)

    return result_md

