"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
CMAKE_ARGS="-DLLAMA_METAL=on"
python -m venv .venv
source .venv/bin/activate

pip install llama-cpp-python

pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

models = [
]

prompt_files = [
        "prompts/capabilities-technical.prompt.md",
        ""
]

from llama_cpp import Llama

llm = Llama(
      model_path="./models/7B/llama-model.gguf",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)
output = llm(
      "Q: Name the planets in the solar system? A: ", # Prompt
      max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion
print(output)


def main():

    for prompt_file in prompt_files:
        print("=" * 120)
        print(f"prompt_file <- prompt_files = {prompt_file}")
        with open(prompt_file, 'r') as f:
            prompt = f.read()
        
        print(prompt)

        for model in models:
            print("." * 120)
            print(f"model <- models = {model}")

            response = chat(model=model, messages=[
                {
                    'role': 'user',
                    'content': prompt
                },
            ])

            txt_response = response['message']['content']

            print(txt_response)
            # or access fields directly from the response object
            # print(response.message.content)

        txt_model = model.replace("/", "-").replace(" ", "_").replace(":", "--")
        txt_prompt = pathlib.Path(prompt_file).stem
        txt_timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        directory = f"{prompt_file}.hwaifs/"
        fn = f"r01--{txt_prompt}--{txt_model}--{txt_timestamp}.md"

        with open(f"{directory}/{fn}", "w") as f:
            f.write(txt_response) 


if __name__ == "__main__":
        main()
