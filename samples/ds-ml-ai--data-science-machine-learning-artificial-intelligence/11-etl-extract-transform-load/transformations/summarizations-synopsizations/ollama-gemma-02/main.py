for img_path in paths:
  try:
    # Read the image file as binary data
    with open(img_path, 'rb') as img_file:
        img_data = img_file.read()
    
    # Convert image to base64 for Ollama
    img_base64 = base64.b64encode(img_data).decode('utf-8')
    
    # Use the correct approach as per Gemma 3 documentation - images at top level
    response = ollama.generate(
        model='gemma3:12b',
        prompt="What's this? Provide a description without leading or trailing text.",
        images=[img_base64],  # Pass base64 encoded image data at top level
        options={"temperature": 0.1}  # Lower temperature for more consistent output
    )
    
    # Extract the caption from the response
    caption = response['response'].strip()
    