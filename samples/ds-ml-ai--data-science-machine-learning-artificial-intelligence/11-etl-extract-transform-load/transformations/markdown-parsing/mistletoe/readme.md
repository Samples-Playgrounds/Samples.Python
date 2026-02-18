# `miseltoe`

*   https://github.com/miyuchina/mistletoe

```python
from mistletoe import Document, HtmlRenderer

with open('foo.md', 'r') as fin:
    with HtmlRenderer() as renderer:     # or: `with HtmlRenderer(AnotherToken1, AnotherToken2) as renderer:`
        doc = Document(fin)              # parse the lines into AST
        rendered = renderer.render(doc)  # render the AST
        # internal lists of tokens to be parsed are automatically reset when exiting this `with` block
```