# Extractous

readme.md

TODO:   does not work with python 3.14 yet

*   https://github.com/yobix-ai/extractous

    Extractous offers a fast and efficient solution for extracting content and metadata from 
    various documents types

```python
from extractous import Extractor

# Create a new extractor
extractor = Extractor()
extractor = extractor.set_extract_string_max_length(1000)
# if you need an xml
# extractor = extractor.set_xml_output(True)

# Extract text from a file
result, metadata = extractor.extract_file_to_string("README.md")
print(result)
print(metadata)
```

