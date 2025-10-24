from IPython import display
from pydantic import BaseModel, Field
from rich import print

file_path = (
    "https://upload.wikimedia.org/wikipedia/commons/9/9f/Swiss_QR-Bill_example.jpg"
)
display.HTML(f"<img src='{file_path}' height='1000'>")

from docling.datamodel.base_models import InputFormat
from docling.document_extractor import DocumentExtractor

extractor = DocumentExtractor(
                                allowed_formats=[
                                                    InputFormat.IMAGE,
                                                    InputFormat.PDF
                                                ]
                            )

result = extractor.extract(
                            source=file_path,
                            template="""
                            {
                            "bill_no": "string", 
                            "total": "float"
                            }""",
                        )
print(result.pages)
