# Smolagents    



Building Agents with Smolagents

    https://www.youtube.com/watch?v=dSGS6-iGhyo

https://github.com/huggingface/hub-tutorials/blob/main/notebooks/02-intro-to-smolagents.ipynb

https://huggingface.co/docs/smolagents/index

https://huggingface.co/LiquidAI/LFM2.5-Encoder-350M-Prompt-Router

https://github.com/tisddm/searxng-mcp


```
import os
from smolagents import GoogleSearchTool, HfApiModel
os.environ["SERPAPI_API_KEY"] = userdata.get('SERPAPI_API_KEY')

model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct", provider="together")

agent = CodeAgent(
    model=model,
    tools=[GoogleSearchTool()]
)
```

https://discuss.huggingface.co/t/is-there-any-agent-that-can-search-google/141016/4

https://smolagents.org/docs/orchestrate-a-multi-agent-system-%F0%9F%A4%96%F0%9F%A4%9D%F0%9F%A4%96/

https://github.com/huggingface/smolagents/blob/main/examples/open_deep_research/README.md

