# llamafile

*   https://github.com/Mozilla-Ocho/llamafile

*   https://huggingface.co/models?other=llamafile

*   https://developers.llamaindex.ai/python/examples/llm/llamafile/

*   https://huggingface.co/models?library=llamafile&sort=likes


```
wget https://huggingface.co/Mozilla/Llama-3.2-1B-Instruct-llamafile/resolve/main/Llama-3.2-1B-Instruct.Q6_K.llamafile
chmod +x Llama-3.2-1B-Instruct.Q6_K.llamafile
./Llama-3.2-1B-Instruct.Q6_K.llamafile --server
```

```python
ai = openai.AsyncOpenAI(base_url="http://localhost:8080/v1", api_key="sk-no-key-required")
response = await ai.chat.completions.create(
                                            messages=[
                                                {"role": "system", "content": "..."}, 
                                                {"role": "user", "content": "..."},
                                            ],
                                            max_tokens=100,
                                            model="Llama-3.2-1B-Instruct.Q6_K.gguf",
                                        )

content = response.choices[0].message.content
```

*   binaries

```
https://huggingface.co/Mozilla/Llama-3.2-1B-Instruct-llamafile/blob/main/Llama-3.2-1B-Instruct.Q6_K.llamafile
https://huggingface.co/Mozilla/Llama-3.2-3B-Instruct-llamafile/blob/main/Llama-3.2-3B-Instruct.Q6_K.llamafile
https://huggingface.co/Mozilla/Meta-Llama-3.1-8B-Instruct-llamafile/resolve/main/Meta-Llama-3.1-8B-Instruct.Q4_K_M.llamafile
https://huggingface.co/Mozilla/gemma-3-1b-it-llamafile/resolve/main/google_gemma-3-1b-it-Q6_K.llamafile
https://huggingface.co/Mozilla/gemma-3-4b-it-llamafile/resolve/main/google_gemma-3-4b-it-Q6_K.llamafile
https://huggingface.co/Mozilla/gemma-3-12b-it-llamafile/resolve/main/google_gemma-3-12b-it-Q4_K_M.llamafile
https://huggingface.co/Mozilla/gemma-3-12b-it-llamafile/resolve/main/google_gemma-3-12b-it-Q4_K_M.llamafile
https://huggingface.co/Mozilla/QwQ-32B-llamafile/resolve/main/Qwen_QwQ-32B-Q4_K_M.llamafile
https://huggingface.co/Mozilla/DeepSeek-R1-Distill-Qwen-14B-llamafile/resolve/main/DeepSeek-R1-Distill-Qwen-14B-Q4_K_M.llamafile
https://huggingface.co/Mozilla/DeepSeek-R1-Distill-Llama-8B-llamafile/resolve/main/DeepSeek-R1-Distill-Llama-8B-Q4_K_M.llamafile
https://huggingface.co/Mozilla/llava-v1.5-7b-llamafile/resolve/main/llava-v1.5-7b-q4.llamafile
https://huggingface.co/Mozilla/Mistral-7B-Instruct-v0.3-llamafile/resolve/main/Mistral-7B-Instruct-v0.3.Q4_0.llamafile
https://huggingface.co/Mozilla/granite-3.2-8b-instruct-llamafile/resolve/main/granite-3.2-8b-instruct-Q4_K_M.llamafile
https://huggingface.co/Mozilla/Phi-3-mini-4k-instruct-llamafile/resolve/main/Phi-3-mini-4k-instruct.F16.llamafile
https://huggingface.co/Mozilla/Mixtral-8x7B-Instruct-v0.1-llamafile/resolve/main/mixtral-8x7b-instruct-v0.1.Q5_K_M.llamafile
https://huggingface.co/Mozilla/OLMo-7B-0424-llamafile/resolve/main/OLMo-7B-0424.Q6_K.llamafile
```


```
https://huggingface.co/Mozilla/e5-mistral-7b-instruct/resolve/main/e5-mistral-7b-instruct-Q5_K_M.llamafile
https://huggingface.co/Mozilla/mxbai-embed-large-v1-llamafile/resolve/main/mxbai-embed-large-v1-f16.llamafile
```

*   https://news.ycombinator.com/item?id=42115016

*   https://justine.lol/oneliners/


```
wget https://huggingface.co/Mozilla/whisperfile/resolve/main/whisper-tiny.en.llamafile
wget https://huggingface.co/Mozilla/whisperfile/resolve/main/raven_poe_64kb.mp3
chmod +x whisper-tiny.en.llamafile
./whisper-tiny.en.llamafile -f raven_poe_64kb.mp3 -pc
```

*   https://huggingface.co/Mozilla/whisperfile