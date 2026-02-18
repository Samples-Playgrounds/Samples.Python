# ExLlamaV2

ExLlamaV2

https://github.com/turboderp-org/exllamav2

```shell
pip install exllamav2
```



Quant means quantized. Quantization is the process of reducing the precision of the model weights by reducing the number of bits. Most models are released in 16 bits, some are released in 8 bits.

You are used to ollama and by extension the .gguf format. The .gguf format is nice in that your tokenizer, config, and model weights are all bundled into one file. You can tell a .gguf file by the ending (it ends in .gguf)

Exllama is a bit different. Exllama expects a FOLDER rather than a file. In that folder contains the model weights (ends in .safetensors), the config.json, tokenizer, and more). You point Exllama to this folder rather than a specific file. To use Exllama you need to look for model repositories ending in exl2-(C)bpw or GPTQ. The C is a number ranging from 2 to 8. This represents the bits per weight (bpw). Higher bpw like 6.0 are more precise models and tend to be smarter at the expense of a larger file size.

In a nutshell ollama is essentially a wrapper around llama.cpp with a model hub and inbuilt rag. Llama.cpp also uses .gguf, but you’ll need to download the models from Huggingface instead. Once they’re downloaded it’s pretty easy to get started.

I’d look at llama-cpp-python. It abstracts the hard parts about llama.cpp and gives you a very easy to use interface for models that’s a bit lower level than ollama


https://www.reddit.com/r/LocalLLaMA/comments/1egbpur/ollama_to_exllamav2/


Exllamav2 IMHO is not better than llama.cpp/Ollama. GGUFs have better quality compression at the given size. Speed is now very similar between the two. Exllamav2 used to be faster by a large margin. It isn't anymore. 

https://www.reddit.com/r/LocalLLaMA/comments/1c9mn1n/whats_the_fastest_local_inference_engine_right/

https://medium.com/@himanshushukla.shukla3/stop-using-llama-cpp-for-multi-gpu-setups-use-vllm-or-exllamav2-instead-73992cf1a1ad

https://medium.com/@himanshushukla.shukla3/stop-using-llama-cpp-for-multi-gpu-setups-use-vllm-or-exllamav2-instead-73992cf1a1ad

