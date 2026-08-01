# Smolagents

*   https://github.com/huggingface/smolagents

    *   https://github.com/samwit/smolagents_examples/blob/main/smol_ollama.py

    *   https://medium.com/@abonia/building-practical-local-ai-agents-with-smolagents-ollama-f92900c51897

    *   https://smolagents.org/docs/agents-guided-tour/

    *   https://huggingface.co/docs/smolagents/reference/models#smolagents.OpenAIModel

*   https://mcpmarket.com/server/searxng-2

*   https://github.com/tisddm/searxng-mcp

```
pip install "smolagents[toolkit]"
```

```python
from smolagents import CodeAgent, WebSearchTool, InferenceClientModel
from smolagents import OpenAIModel

# model = InferenceClientModel()
OpenAIModel(
            model_id="Qwen3.6-35B-A3B",
            api_base="http://127.0.0.1:11454",
            api_key=os.environ["OPENAI_API_KEY"],
            temperature=0.7,
            max_tokens=255000,
            top_p=0.9,
            agent = CodeAgent(
                                tools=[
                                        WebSearchTool()
                                        ],
                                model=model,
                                stream_outputs=True)

agent.run(
            """
            How many seconds would it take for a leopard at full speed to run through Pont des Arts?
            """
        )
```

```python
from smolagents import CodeAgent, LiteLLMModel, ToolCollection
from mcp import StdioServerParameters

# Configure the SearXNG MCP server
server_parameters = StdioServerParameters(
    command="node",
    args=["path/to/searxng-mcp/build/index.js"],
    env={
        "SEARXNG_URL": "https://your-searxng-instance.com",
        "SEARXNG_USERNAME": "your_username",  # Optional
        "SEARXNG_PASSWORD": "your_password"   # Optional
    }
)

# Create a tool collection from the MCP server
with ToolCollection.from_mcp(server_parameters) as tool_collection:
    # Initialize your LLM model
    model = LiteLLMModel(
        model_id="your-model-id",
        api_key="your-api-key",
        temperature=0.7
    )
    
    # Create an agent with the search tools
    search_agent = CodeAgent(
        name="search_agent",
        tools=tool_collection.tools,
        model=model
    )
    
    # Run the agent with a search prompt
    result = search_agent.run(
        "Perform a search about: 'climate change solutions' and summarize the top 5 results."
    )
    
    print(result)
```
