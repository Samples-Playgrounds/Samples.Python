import os
from pathlib import Path
import pdfplumber
from pdfplumber.utils import extract_text, get_bbox_overlap, obj_to_bbox

def extract_text_to_file_from_pdf_document (source: str) -> str:

    result_txt = ""

    with pdfplumber.open(source) as pdf:
        for page in pdf.pages:
            result_txt = result_txt + page.extract_text()

    directory = f"{source}.hwaifs/text/python/pdfplumber/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.txt", "w") as f:
        f.write(result_txt)

    return result_txt


def extract_markdown_to_file_from_pdf_document (source: str) -> str:

    result_txt = ""

    all_text = []

    with pdfplumber.open(source) as pdf:
        for page in pdf.pages:
            filtered_page = page
            chars = filtered_page.chars
            for table in page.find_tables():
                first_table_char = page.crop(table.bbox).chars[0]
                filtered_page = filtered_page.filter(lambda obj: 
                    get_bbox_overlap(obj_to_bbox(obj), table.bbox) is None
                )
                chars = filtered_page.chars
                df = pd.DataFrame(table.extract())
                df.columns = df.iloc[0]
                markdown = df.drop(0).to_markdown(index=False)
                chars.append(first_table_char | {"text": markdown})
            page_text = extract_text(chars, layout=True)
            all_text.append(page_text)
        pdf.close()

    directory = f"{source}.hwaifs/text/python/pdfplumber/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    # save to file
    with open(f"{directory}/content.md", "w") as f:
        f.write(result_txt)

    return "\n".join(all_text)


