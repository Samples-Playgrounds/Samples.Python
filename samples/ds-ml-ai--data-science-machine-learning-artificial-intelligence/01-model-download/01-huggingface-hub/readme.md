# 

## Locations

### HuggingFace

```shell
$HOME/.cache/huggingface/hub
$HOME/.cache/huggingface/xet
```

### Llama.cpp

```shell
$HOME$/Library/Caches/llama.cpp/
```

## Diverse

*   https://github.com/ggml-org/llama.cpp/discussions/2948

*   https://github.com/Hannibal046/Awesome-LLM

*   https://huggingface.co/docs/hub/en/models-downloading


```
from huggingface_hub import hf_hub_download
downloaded_model_path = hf_hub_download(
                                        repo_id="CompVis/stable-diffusion-v-1-4-original",
                                        filename="sd-v1-4.ckpt",
                                        use_auth_token=True
                                        ); 
print(downloaded_model_path)'
```

*   https://www.baeldung.com/cs/hugging-face-model-download


