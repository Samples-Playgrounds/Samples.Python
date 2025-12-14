# vLLM

*   https://github.com/vllm-project/vllm

*   https://pypi.org/project/vllm/

*   https://docs.vllm.ai/en/latest/usage/

```shell
pip install vllm    
```

```python
from vllm import LLM

# Initialize the vLLM engine.
llm = LLM(model="facebook/opt-125m")
```

```shell
vllm serve microsoft/phi-1_5 --trust-remote-code
```

```
open -a "" http://0.0.0.0:8000/
```
*   https://docs.vllm.ai/en/v0.6.5/getting_started/installation.html

*   https://medium.com/@rohitkhatana/installing-vllm-on-macos-a-step-by-step-guide-bbbf673461af
    
*   https://towardsdev.com/vllm-a-quick-start-cf1c48aa5890
