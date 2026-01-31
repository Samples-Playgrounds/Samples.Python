# `keras-ocr`

readme.md

*   https://github.com/faustomorales/keras-ocr

*   https://keras-ocr.readthedocs.io/en/latest/


```shell
pip install keras-ocr
```

```python
import easyocr
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
result = reader.readtext('chinese.jpg')
```

*   https://medium.com/@mdskhan0x44/running-keras-ocr-python-library-in-2025-1b6fcbbe023c
