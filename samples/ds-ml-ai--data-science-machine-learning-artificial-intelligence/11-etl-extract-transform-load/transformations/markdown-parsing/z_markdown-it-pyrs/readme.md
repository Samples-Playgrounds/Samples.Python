# `markdown-it-pyrs`

```
markdown-it-pyrs
segmentation fault
macosx
```

*   https://pypi.org/project/markdown-it-pyrs/

*   https://waylonwalker.com/thoughts-332/

*   https://markdown-it-py.readthedocs.io/en/latest/performance.html

```shell
pip install markdown-it-pyrs
```

```python
from markdown_it_pyrs import MarkdownIt

md = MarkdownIt("commonmark").enable("table")
md.render("# Hello, world!")
# '<h1>Hello, world!</h1>\n'

md = (
  MarkdownIt("commonmark")
  .enable("table")
  .enable_many(["linkify", "strikethrough"])
)
node = md.tree("# Hello, world!")
print(node.walk())
# [Node(root), Node(heading), Node(text)]
print(node.pretty(srcmap=True, meta=True))
```

