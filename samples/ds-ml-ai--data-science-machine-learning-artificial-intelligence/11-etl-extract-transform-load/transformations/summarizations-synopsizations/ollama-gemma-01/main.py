llm = Ollama(model="gemma3", request_timeout=360.0)
response = llm.chat([ChatMessage("What's this? Provide a description without leading or trailing text.", additional_kwargs={"images": [ImageDocument(image_path=image_path)]})])

