# `commonmark`

readme.md

*   https://pypi.org/project/commonmark/

```shell
pip install commonmark
```

```python
import commonmark
parser = commonmark.Parser()
ast = parser.parse("Hello *World*")

renderer = commonmark.HtmlRenderer()
html = renderer.render(ast)
print(html) # <p>Hello <em>World</em><p/>

# inspecting the abstract syntax tree
json = commonmark.dumpJSON(ast)
commonmark.dumpAST(ast) # pretty print generated AST structure
```


