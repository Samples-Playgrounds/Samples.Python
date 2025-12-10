# DocStrange

readme.md

*   https://github.com/NanoNets/docstrange


```python
from docstrange import DocumentExtractor

# Initialize extractor (cloud mode by default)
extractor = DocumentExtractor()

# Convert any document to clean markdown
result = extractor.extract("document.pdf")
markdown = result.extract_markdown()
print(markdown)
```


```python
from docstrange import DocumentExtractor

# Extract document as structured JSON
extractor = DocumentExtractor()
result = extractor.extract("document.pdf")

# Get all important data as flat JSON
json_data = result.extract_data()
print(json_data)
```

```python
from docstrange import DocumentExtractor

# Extract only the fields you need
extractor = DocumentExtractor()
result = extractor.extract("invoice.pdf")

# Specify exactly which fields to extract
fields = result.extract_data(specified_fields=[
    "invoice_number", "total_amount", "vendor_name", "due_date"
])
print(fields)
```

```python
from docstrange import DocumentExtractor

# Extract data conforming to your schema
extractor = DocumentExtractor()
result = extractor.extract("contract.pdf")

# Define your required structure
schema = {
    "contract_number": "string",
    "parties": ["string"],
    "total_value": "number",
    "start_date": "string",
    "terms": ["string"]
}

structured_data = result.extract_data(json_schema=schema)
print(structured_data)
```