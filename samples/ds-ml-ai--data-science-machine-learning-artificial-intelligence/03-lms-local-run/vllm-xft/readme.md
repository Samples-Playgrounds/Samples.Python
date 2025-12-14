# `vllm-xft`

*   https://pypi.org/project/vllm-xft/

```shell
pip install vllm-xft
```


```shell
python \
    -m vllm.entrypoints.openai.api_server \
        --model /data/llama-2-7b-chat-cpu \
        --tokenizer /data/llama-2-7b-chat-hf \
        --dtype fp16 \
        --kv-cache-dtype fp16 \
        --served-model-name xft \
        --port 8000 \
        --trust-remote-code \
```