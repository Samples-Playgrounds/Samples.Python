# Text from Images

*   https://community.palantir.com/t/guide-parsing-pdf-files-using-python-with-tesseract-ocr/1347

*   https://medevel.com/os-ocr-libraris-and-frameworks/

## Image to Text

*   https://pypi.org/project/pytesseract/

*   https://github.com/sirfz/tesserocr

*   https://github.com/charlesw/tesseract

*   https://github.com/tesseract-ocr/tesseract

*   https://tesseract-ocr.github.io/

*   https://github.com/huridocs/pdf-document-layout-analysis

*   https://www.nutrient.io/blog/tesseract-python-guide/

*   https://www.nutrient.io/blog/how-to-use-tesseract-ocr-in-python/



*   pytesseract

    *   great for documents

    ```python
    import pytesseract

    pytesseract.image_to_string(filename, lang='eng')
    ```

*   EasyOCR

    *   https://github.com/JaidedAI/EasyOCR

        ```
        pip install easyocr
        ```

        ```python
        import easyocr
        import pandas as pd
        reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
        result = reader.readtext('chinese.jpg')
        pd.DataFrame(result, columns['bbox', 'text', 'conf'])
        pd.DataFrame(results[0], columns=['text', 'bbox']) 
        ```

*   keras_ocr

        *   https://github.com/faustomorales/keras-ocr

        *   https://keras-ocr.readthedocs.io/en/latest/

        ```
        pip install keras-ocr
        ```

        ```python
        import keras_ocr

        # keras-ocr will automatically download pretrained
        # weights for the detector and recognizer.
        pipeline = keras_ocr.pipeline.Pipeline()
        results = pipeline.recognize([img_fns[11]])
        pd.DataFrame(results[0], columns=['text', 'bbox'])
        ```

*   Spire.OCR

    *   https://www.kaggle.com/datasets/robikscube/textocr-text-extraction-from-images-dataset

## Diverse

*   https://stackoverflow.com/questions/78479905/extract-text-from-image-using-tessaract-and-opencv

*   https://stackoverflow.com/questions/46260970/extracting-text-out-of-images

*   https://www.geeksforgeeks.org/python/how-to-extract-text-from-images-with-python/

*   https://medium.com/@alice.yang_10652/extract-text-from-images-and-scanned-pdfs-with-python-2087cb1e0a7b

*   https://medium.com/data-science/top-5-python-libraries-for-extracting-text-from-images-c29863b2f3d