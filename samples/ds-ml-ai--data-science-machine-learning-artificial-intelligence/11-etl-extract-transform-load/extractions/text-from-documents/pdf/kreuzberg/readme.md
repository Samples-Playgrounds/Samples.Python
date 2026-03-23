# Kreuzberg

readme.md

*   https://github.com/kreuzberg-dev/kreuzberg

*   https://kreuzberg.dev/

*   https://www.reddit.com/r/Rag/comments/1pn2fxv/kreuzberg_v400rc8_is_available/

*   polyglot multi-lingual

    *   python

        *   https://github.com/kreuzberg-dev/kreuzberg/blob/main/packages/python/README.md

    *   c#

        *   https://github.com/kreuzberg-dev/kreuzberg/blob/main/packages/csharp/README.md

https://github.com/kreuzberg-dev/kreuzberg/blob/main/skills/kreuzberg/SKILL.md

https://pypi.org/project/kreuzberg/4.0.0rc11/

https://news.ycombinator.com/item?id=43057375

https://pypi.org/project/kreuzberg/

https://dev.to/kreuzberg/how-to-extract-text-from-pdf-in-python-2026-3a97

```shell
brew install onnxruntime
brew install tesseract
brew install libreoffice
```



```csharp
using Kreuzberg;

var result = KreuzbergClient.ExtractFileSync("document.pdf");
Console.WriteLine(result.Content);
```

```shell
pip install kreuzberg
pip install "kreuzberg[easyocr]"
pip install "kreuzberg[paddleocr]"
pip install "kreuzberg[all]"
```

```python
from kreuzberg import extract_file_sync

result = extract_file_sync("document.pdf")
print(result.content)
```

```
from kreuzberg import extract_file

result = await extract_file("document.pdf")
print(result.content)
```

```
from kreuzberg import batch_extract_files

files = ["doc1.pdf", "doc2.docx", "doc3.xlsx"]
results = await batch_extract_files(files)

for result in results:
    print(result.content)
```