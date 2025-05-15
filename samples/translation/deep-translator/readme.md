# deep-translator

readme.md

*   https://pypi.org/project/deep-translator/

*   https://deep-translator.readthedocs.io/en/latest/README.html

```bash
python3.13 -m venv .venv
source .venv/bin/activate

pip3.13 install -U deep-translator
# add support for docx translation
pip3.13 install deep-translator[docx]
# add support for pdf translation
pip3.13 install deep-translator[pdf]
# add support for ChatGpt
pip3.13 install deep-translator[ai]

pip3.13 freeze > requirements.txt
```

```bash
pip3.13 install -r requirements.txt
python3.13 translate.py
```



```python
from deep_translator import GoogleTranslator

text_en = "keep it up, you are awesome"
# Use any translator you like, in this example GoogleTranslator
translated = GoogleTranslator(source='auto', target='de').translate(text_en)  

# output -> Weiter so, du bist großartig
print(translated)
```