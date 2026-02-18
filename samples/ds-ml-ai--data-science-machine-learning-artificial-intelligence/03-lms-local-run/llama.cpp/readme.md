# `llama.cpp`

readme.md

*   https://github.com/abetlen/llama-cpp-python


```bash
CMAKE_ARGS="-DLLAMA_METAL=on"
pip install llama-cpp-python
```

*     https://github.com/abetlen/llama-cpp-python

```python
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
```

```python
from llama_cpp import Llama
llm = Llama(
      model_path="path/to/llama-2/llama-model.gguf",
      chat_format="llama-2"
)
llm.create_chat_completion(
      messages = [
          {"role": "system", "content": "You are an assistant who perfectly describes images."},
          {
              "role": "user",
              "content": "Describe this image in detail please."
          }
      ]
)
```

*     https://christophergs.com/blog/running-open-source-llms-in-python

*     https://medium.com/@aleksej.gudkov/llama-cpp-python-examples-a-guide-to-using-llama-models-with-python-1df9ba7a5fcd