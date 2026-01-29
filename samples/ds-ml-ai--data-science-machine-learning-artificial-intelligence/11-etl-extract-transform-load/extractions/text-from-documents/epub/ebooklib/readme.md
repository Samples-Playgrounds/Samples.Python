# Ebboklib

readme.md

*   https://github.com/aerkalov/ebooklib

*   https://docs.sourcefabric.org/projects/ebooklib/en/latest/

*   https://gist.github.com/robmcelhinney/b16f7db3a31330bb8d342c7ae03435b2

```python
import ebooklib
from ebooklib import epub

book = epub.read_epub('test.epub')

for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    print doc
```

*   https://pypi.org/project/beautifulsoup4/
