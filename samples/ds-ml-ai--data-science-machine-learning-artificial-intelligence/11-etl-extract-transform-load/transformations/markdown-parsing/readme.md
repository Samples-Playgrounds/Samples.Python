# 

https://mistune.lepture.com/en/latest/guide.html

https://github.com/miyuchina/mistletoe

https://github.com/executablebooks/markdown-it-py

```
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin

md = (
    MarkdownIt('commonmark', {'breaks':True,'html':True})
    .use(front_matter_plugin)
    .use(footnote_plugin)
    .enable('table')
)
text = ("""
---
a: 1
---

a | b
- | -
1 | 2

A footnote [^1]

[^1]: some details
""")
tokens = md.parse(text)
html_text = md.render(text)

## To export the html to a file, uncomment the lines below:
# from pathlib import Path
# Path("output.html").write_text(html_text)
```



https://github.com/frostming/marko
