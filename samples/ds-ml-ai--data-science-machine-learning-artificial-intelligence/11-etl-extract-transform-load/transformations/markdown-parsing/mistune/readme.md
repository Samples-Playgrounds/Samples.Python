# `mistune`

*   https://github.com/lepture/mistune

*   https://mistune.lepture.com/en/latest/

*   

```shell
$ pip install mistune
```

```python
import mistune

# convert to html
mistune.html(your_markdown_text)

# generate AST
markdown = mistune.create_markdown(renderer=None)

# generate AST
markdown = mistune.create_markdown(renderer='ast')
```