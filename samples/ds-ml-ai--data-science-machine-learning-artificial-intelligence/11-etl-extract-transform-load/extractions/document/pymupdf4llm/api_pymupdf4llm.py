import pymupdf4llm


def covert_pdf_file_to_markdown (source: str) -> str:

    result_md = pymupdf4llm.to_markdown(source)

    return result_md
