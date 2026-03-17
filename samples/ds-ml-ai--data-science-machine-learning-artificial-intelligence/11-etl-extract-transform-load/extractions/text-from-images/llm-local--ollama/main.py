import os
import json
import base64
import ollama
import time
from pathlib import Path

# --- Configuration ---
INPUT_DIR = "input"
MODELS = [
    {"name": "granite3.2-vision", "output_dir": "granite-vision-output"},
    {"name": "llama3.2-vision", "output_dir": "llama-vision-output"},
]

# --- Helper Functions ---
def is_image_file(filename):
    """Checks if a file has a common image extension."""
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff"}
    return Path(filename).suffix.lower() in image_extensions

def get_base64_image(image_path):
    """Reads an image file and returns its Base64-encoded string."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except IOError as e:
        print(f"Error reading image file {image_path}: {e}")
        return None

def process_image_with_ollama(model_name, image_path, base64_image):
    """Sends an image to the Ollama model for text extraction."""
    print(f"Processing image with {model_name}: {image_path}")
    start_time = time.time()
    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": "Extract all text from this image.",
                    "images": [base64_image],
                }
            ],
        )
        end_time = time.time()
        extracted_text = response['message']['content']
        elapsed_time = end_time - start_time
        return extracted_text, elapsed_time
    except Exception as e:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Error with Ollama API for {image_path} using model {model_name}: {e}")
        return None, elapsed_time

def save_to_json(filepath, data):
    """Saves data to a JSON file."""
    try:
        with open(filepath, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Successfully saved text to {filepath}")
    except IOError as e:
        print(f"Error writing to JSON file {filepath}: {e}")

# --- Main Application Logic ---
def main():
    """Main function to run the OCR process for multiple models."""
    print("Starting Ollama OCR application...")

    # Ensure the input directory exists
    if not Path(INPUT_DIR).exists():
        print(f"Error: The input directory '{INPUT_DIR}' does not exist. Please create it and add images.")
        return

    # Create a list of all image paths to process
    image_paths = []
    for root, _, files in os.walk(INPUT_DIR):
        for filename in files:
            if is_image_file(filename):
                image_paths.append(Path(root) / filename)

    if not image_paths:
        print(f"No image files found in '{INPUT_DIR}'. Please add images to the folder.")
        return

    # Process images with each model specified in the MODELS list
    for model_info in MODELS:
        model_name = model_info["name"]
        output_dir = model_info["output_dir"]
        
        # Ensure the model-specific output directory exists
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        print(f"\nProcessing images with model: {model_name}")

        for image_path in image_paths:
            # Get the Base64 representation of the image
            base64_image = get_base64_image(image_path)
            if not base64_image:
                continue  # Skip to the next file if there was an error

            # Process the image with the Ollama model and get the elapsed time
            extracted_text, elapsed_time = process_image_with_ollama(model_name, image_path, base64_image)
            
            # Print the elapsed time for the current image
            print(f"  - Time elapsed for this photo: {elapsed_time:.2f} seconds.")

            if extracted_text:
                # Construct the output filename, preserving the relative path
                relative_path = image_path.relative_to(INPUT_DIR)
                output_sub_dir = Path(output_dir) / relative_path.parent
                
                # Create subdirectories in the output folder to mirror the input folder structure
                output_sub_dir.mkdir(parents=True, exist_ok=True)
                
                # New filename format: {model_name}_{original_filename_stem}.json
                output_filename = f"{model_name.replace(':', '_')}_{image_path.stem}.json"
                output_filepath = output_sub_dir / output_filename
                
                # Prepare data for JSON file, including the elapsed time
                json_data = {
                    "original_image_path": str(image_path),
                    "extracted_text": extracted_text,
                    "model_used": model_name,
                    "processing_time_seconds": round(elapsed_time, 2)
                }
                
                # Save the extracted data
                save_to_json(output_filepath, json_data)
            else:
                print(f"Could not extract text from {image_path} with model {model_name}. Skipping.")

    print("\nOllama OCR application finished.")

if __name__ == "__main__":
    main()
