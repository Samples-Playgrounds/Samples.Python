"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install easyocr
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_text_extraction_from_images_EasyOCR as api

root="../../../../../../data/images/"

# document per local path or URL
sources = [
    f"{root}/maui/architecture-diagram.png",
    f"{root}/maui/maui-overview.png",
    f"{root}/android/architecture1.png",
    f"{root}/crime-orgs/judo/Screenshot 2025-11-18 at 13.00.30.png",
    f"{root}/crime-orgs/judo/Screenshot 2025-11-18 at 13.00.30.png",
    f"{root}/dontetconf/2025/Screenshot 2025-11-17 at 11.35.46.edited.png",
    f"{root}/dontetconf/2025/Screenshot 2025-11-17 at 11.35.46.png"
]


def main():
   for source in sources:
      print(f"easyocr <- source = {source}")
      text = api.extract_text_to_file_from_image(source)
      print(f"  text = {text}")


if __name__ == '__main__':
    main()
