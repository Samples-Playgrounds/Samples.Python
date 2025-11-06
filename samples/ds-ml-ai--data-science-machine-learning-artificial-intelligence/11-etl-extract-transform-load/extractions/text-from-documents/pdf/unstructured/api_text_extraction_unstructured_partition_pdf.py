from unstructured.partition.pdf import partition_pdf
from unstructured.staging.base import elements_to_json
import os
from pathlib import Path


def extract_text_to_file_from_pdf_document (source: str) -> str:

    # Returns a List[Element] present in the pages of the parsed pdf document
    elements = partition_pdf(source)

    result_txt = "\n\n".join([str(el) for el in elements])

    directory = f"{source}.hwaifs/text/python/unstructured/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}content.txt", "w") as f:
        f.write(result_txt) 

    elements_to_json(
                        elements=elements, 
                        filename=f"{directory}contents.json",
                    )

    return result_txt
