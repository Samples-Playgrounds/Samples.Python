from pdf2image import convert_from_path
from pathlib import Path


def extract_pages_to_images (source: str) -> str:
    """
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/images/py/pdf2image/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    pages = convert_from_path(source, 500)

    for count, page in enumerate(pages):
        page.save(f"{directory}/p{count}.jpg", 'JPEG')
