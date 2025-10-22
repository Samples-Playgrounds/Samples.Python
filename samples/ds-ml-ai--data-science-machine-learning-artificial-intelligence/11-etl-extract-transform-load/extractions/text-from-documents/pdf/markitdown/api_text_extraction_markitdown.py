import os
from pathlib import Path
from markitdown import MarkItDown

def extract_text_to_file_from_any_document (source: str) -> str:
    md = MarkItDown()
    result_md = md.convert(source).text_content

    directory = f"{source}.hwaifs/text/python/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/markitdown.md", "w") as f:
        f.write(result_md)

    return result_md
