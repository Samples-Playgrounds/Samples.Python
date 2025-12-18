

*   https://github.com/ankushshah89/python-docx2txt

```
pip install docx2txt
```

```
import docx2txt

# extract text
text = docx2txt.process("file.docx")

# extract text and write images in /tmp/img_dir
text = docx2txt.process("file.docx", "/tmp/img_dir") 
```