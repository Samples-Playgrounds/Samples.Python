"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install keras-ocr
pip install tensorflow==2.15
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_text_extraction_from_images_keras_ocr as api

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

# Get a set of three example images
images = [
    keras_ocr.tools.read(url) for url in [
        'https://upload.wikimedia.org/wikipedia/commons/b/bd/Army_Reserves_Recruitment_Banner_MOD_45156284.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/e8/FseeG2QeLXo.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/b/b4/EUBanana-500x112.jpg'
    ]
]

def main():
   for source in sources:
      print(f"keras-ocr <- source = {source}")
      text = api.extract_text_to_file_from_image(source)
      print(f"  text = {text}")

#   for img in images:
#      print(f"keras-ocr <- source = {source}")
#      text = api.extract_text_to_file_from_image(source)
#      print(f"  text = {text}")

if __name__ == '__main__':
    main()
