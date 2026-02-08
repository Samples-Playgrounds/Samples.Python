# epub2txt


*   https://github.com/kevinboone/epub2txt2

*   https://pypi.org/project/epub2txt/

```shell
pip install epub2txt
# pip install epub2txt -U  # to upgrade
```

```python
from epub2txt import epub2txt
# from a url to epub
url = "https://github.com/ffreemt/tmx2epub/raw/master/tests/1.tmx.epub"
res = epub2txt(url)

# from a local epub file
filepath = r"tests\test.epub"
res = epub2txt(filepath)

# output as a list of chapters
ch_list = epub2txt(filepath, outputlist=True)
# chapter titles will be available as epub2txt.content_titles if available
```