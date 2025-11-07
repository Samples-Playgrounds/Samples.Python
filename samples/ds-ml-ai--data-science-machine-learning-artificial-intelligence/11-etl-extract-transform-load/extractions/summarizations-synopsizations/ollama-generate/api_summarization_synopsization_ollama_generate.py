import ollama 
import base64
from pathlib import Path
import datetime

def summarize_synopsize_image_with_model_in_n_sentences (
                                                            source: str,
                                                            model="llama3.2-vision:latest",
                                                            prompt="Describe image in 5 sentences",
                                                            number_of_sentences = 5
                                                        ) -> str:

    # Read the image file as binary data
    with open(source, 'rb') as img_file:
        img_data = img_file.read()

    # Convert image to base64 for Ollama
    img_base64 = base64.b64encode(img_data).decode('utf-8')

    prompt = f"{prompt}\nProvide the response in {number_of_sentences} sentences."

    # Use the correct approach as per Gemma 3 documentation - images at top level
    response = ollama.generate(
                                model,
                                prompt,
                                # Pass base64 encoded image data at top level
                                images=[img_base64],
                                # Lower temperature for more consistent output
                                options={"temperature": 0.1}
                                )

    # Extract the caption from the response
    result = response['response'].strip()

    model = model.replace(":", "--")
    directory = f"{source}.hwaifs/summarization_synopsization/python/ollama-generate/{model}"
    Path(directory).mkdir(parents=True, exist_ok=True)

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")

    with open(f"{directory}/prompt-{number_of_sentences}-{timestamp}.md", "w") as f:
        f.write(prompt)
    with open(f"{directory}/response-{number_of_sentences}-{timestamp}.md", "w") as f:
        f.write(result)

    return result


#for img_path in paths:
#  try:
#    # Read the image file as binary data
#    with open(img_path, 'rb') as img_file:
#        img_data = img_file.read()
#    
#    # Convert image to base64 for Ollama
#    img_base64 = base64.b64encode(img_data).decode('utf-8')
#    
#    # Use the correct approach as per Gemma 3 documentation - images at top level
#    response = ollama.generate(
#        # model='gemma3:12b',
#        model='llama3.2-vision:latest',
#        prompt="What's this? Provide a description without leading or trailing text.",
#        images=[img_base64],  # Pass base64 encoded image data at top level
#        options={"temperature": 0.1}  # Lower temperature for more consistent output
#    )
#    
#    # Extract the caption from the response
#    caption = response['response'].strip()
