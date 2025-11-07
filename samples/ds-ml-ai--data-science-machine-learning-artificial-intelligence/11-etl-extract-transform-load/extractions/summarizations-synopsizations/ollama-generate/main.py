"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install ollama
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

root="/Users/Shared/Projects/d/Samples-Playgrounds/gh/Python/data/images/"

sources = [
          f"{root}/maui/architecture-diagram.png",
          f"{root}/maui/maui-overview.png",
          f"{root}/android/architecture1.png"
        ]
models = [
            "llama3.2-vision:latest",
            "gemma3:latest",
            "gemma3:4b",
            "gemma3:12b",
            "gemma3:27b",
            "deepseek-r1:latest",
            "phi3.5:latest",
            "phi:latest",
            #"gpt-oss:120b"                 # 65GB Too large for MBP M4 128 GB    
            "gpt-oss:20b",
            "gpt-oss:latest",
            "phind-codellama:34b",
            #"mistral-large:latest",        # 73GB Too large for MBP M4 128 GB
            "phind-codellama:latest",       
            #"mistral-large:123b",
            "codegemma:7b",
            "codegemma:latest",
            "codellama:70b",
            #"deepseek-coder-v2:236b",      # 132GB Too large for MBP M4 128 GB
            "deepseek-coder:latest",
            "deepseek-coder-v2:latest",
            "llama3.3:latest",
            "deepseek-coder:33b",
            "all-minilm:latest",
            "qwq:latest",
            "marco-o1:latest",
            "phi4:latest",
            "nomic-embed-text:latest",
]

prompts = [
          """
          Describe the image
          """,
          """
          What's this? Provide a description without leading or trailing text.
          """
]

numbers_of_sentences = [
                        3,
                        5,
                        10  
]

import api_summarization_synopsization_ollama_generate as api



def main():
  for source in sources:
    for model in models:
      for prompt in prompts:
        for number_of_sentences in numbers_of_sentences:
          print("=" * 120)
          print(f"source                    = {source}")
          print(f"  model                   = {model}")
          print(f"    prompt                = {prompt}")
          print(f"      number_of_sentences = {number_of_sentences}")
          response = api.summarize_synopsize_image_with_model_in_n_sentences(
                                                                                source,
                                                                                model,
                                                                                prompt,
                                                                                number_of_sentences
                                                                            )

          print(f"      response = ")
          print(f"      {response}")
                                                              


if __name__ == '__main__':
    main()
