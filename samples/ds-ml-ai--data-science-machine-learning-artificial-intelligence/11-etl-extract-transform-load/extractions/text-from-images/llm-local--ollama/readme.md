

https://alain-airom.medium.com/the-future-of-document-scanning-a-look-at-llm-powered-ocr-b7d92a0556f9


pip install ollama

https://dev.to/karavanjo/how-to-run-a-local-model-for-text-recognition-in-images-2d6a

https://github.com/karavanjo/dev-content/tree/main/llama-local-run

pip install ollama-ocr

from ollama_ocr import OCRProcessor

ocr = OCRProcessor(model_name='llama3.2-vision:11b')

result = ocr.process_image(
    image_path="./your_image.jpg",
    format_type="text"
)
print(result)