# Translation

readme.md


```
# Use any translator you like, in this example GoogleTranslator
translated = GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")  
# output -> Weiter so, du bist großartig
```

from deep_translator import GoogleTranslator

proxies_example = {
    "https": "34.195.196.27:8080",
    "http": "34.195.196.27:8080"
}
translated = GoogleTranslator(source='auto', target='de', proxies=proxies_example).translate("keep it up, you are awesome")  
# output -> Weiter so, du bist großartig

from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

Google Translator

PONS

Linguee

Mymemory

https://github.com/nidhaloff/deep-translator

https://github.com/Saravananslb/py-googletranslation

https://github.com/ssut/py-googletrans

https://pypi.org/project/googletrans/



## Diverse

*   https://medium.com/analytics-vidhya/how-to-translate-text-with-python-9d203139dcf5

*   https://jackmckew.dev/translating-text-in-python.html

*   https://www.kaggle.com/code/khotijahs1/how-to-translate-and-detect-language-in-python

https://stackoverflow.com/questions/72912512/i-got-the-translation-from-googletrans-working-in-python-but-want-to-pull-just-t

https://medium.com/@musowir_u/language-translation-with-python-a-beginners-guide-using-googletrans-library-6df86223a7b5
