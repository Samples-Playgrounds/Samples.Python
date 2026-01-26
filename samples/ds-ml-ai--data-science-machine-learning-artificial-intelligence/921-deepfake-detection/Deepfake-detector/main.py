"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install temsorflow
pip install deepfake_detector
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_deepfake_detection as api

def main():
    for source in sources:
        result = api.detect_deepfake_from_image(source)
        print(result)


if __name__ == '__main__':
    main()

