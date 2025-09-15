# Unstructured

readme.md

```shell
rm -fr .venv
python -m venv .venv
source .venv/bin/activate
pip install "unstructured[all-docs]"
pip freeze > requirements.txt
```

```bash
pip install -r requirements.txt
python main.py
```

```shell
brew \
    install \
        libmagic \
        poppler \
        tesseract
```

*   https://unstructured.io/

*   https://pypi.org/project/unstructured/

*   https://pypi.org/project/unstructured.pytesseract/