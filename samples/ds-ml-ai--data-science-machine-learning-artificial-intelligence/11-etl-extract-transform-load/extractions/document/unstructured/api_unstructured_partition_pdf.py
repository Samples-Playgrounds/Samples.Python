from unstructured.partition.pdf import partition_pdf

def covert_pdf_file_to_text (source: str) -> str:

    # Returns a List[Element] present in the pages of the parsed pdf document
    elements = partition_pdf(source)

    result_txt = "\n\n".join([str(el) for el in elements])

    return result_txt
