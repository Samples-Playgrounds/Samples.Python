# `mdextractor`

readme.md

*   code blocks only

*   https://pypi.org/project/mdextractor/

*   https://github.com/chigwell/mdextractor

```shell
pip install mdextractor
```

```python
from mdextractor import extract_md_blocks

text = """
\`\`\`python
print("Hello, Markdown!")
\`\`\`
"""

blocks = extract_md_blocks(text)
print(blocks)
# Output: ['print("Hello, Markdown!")']
```


