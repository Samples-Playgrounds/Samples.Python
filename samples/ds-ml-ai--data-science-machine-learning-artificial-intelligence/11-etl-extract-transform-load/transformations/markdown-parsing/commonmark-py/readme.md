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

```python
import commonmark 
parser = commonmark.Parser() 
ast = parser.parse(p.content)

paragraphs = '' for node in ast.walker():
    if node[0].t == "paragraph":
        paragraphs += " "
        paragraphs += node[0].first_child.literal

```


*   https://dev.to/waylonwalker/using-a-python-markdown-ast-to-find-all-paragraphs-2876

*   https://waylonwalker.com/python-markdown-ast-paragraph/