"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install pypdf
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""


from pypdf import PdfWriter

from pathlib import Path

rootdir = Path('/Volumes/xFAT-1TB-2/e/personal-private/judo/HJS/01-pravno/DORH/02-kaznena-prijava-koraci/TODO/mails/20260199-01-sindikati/')
# Return a list of regular files only, not directories
file_list = [f for f in rootdir.glob('**/[!._]*.pdf') if f.is_file()]

for file_path in file_list:
    if \
        '4.1.1-Realizacija' in str(file_path) \
        or \
        'HJS grubo kršenje ugovora MINTS' in str(file_path) \
        :
        continue

    print(f"Reading file_path           : {file_path}")
    writer = PdfWriter(clone_from=file_path)
    for page in writer.pages:
        page.compress_content_streams()  # This is CPU intensive!
    file_path_compressed = file_path.with_name(file_path.stem + '.compressed.pdf')
    writer.write(file_path_compressed)
    print(f"Saving compressed PDF to     : {file_path_compressed}")
