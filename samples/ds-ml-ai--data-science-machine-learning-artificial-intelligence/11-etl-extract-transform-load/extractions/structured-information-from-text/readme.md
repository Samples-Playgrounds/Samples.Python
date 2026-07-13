
Data Analysis

https://platform.claude.com/cookbook/managed-agents-data-analyst-agent

https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/data_analyst_agent.ipynb

*   OmniParse

    *   web app
    
        *   https://github.com/adithya-s-k/omniparse

        *   document ingestion

            *   Marker

                *   https://github.com/datalab-to/marker

    *   python library
    
        *   https://github.com/The-Swarm-Corporation/OmniParse

            ```shell
            pip install omniparse
            ```

            ```python
            from omniparse.main import OmniParse
            from omniparse.prebuilt_agent import model

            parser = OmniParse(
                model=model,
                document_name="doc.pdf",
                db_n_results=3,
                limit_tokens=1000,
                collection_name="omniparse_db",
            )

            context = parser.run("What is the total amount due?")
            print(context)
            ```


*   OmniParser

    *   https://microsoft.github.io/OmniParser/

    *   screen reader
    
*   Instructor
    
    *   https://python.useinstructor.com/
    
    *   https://github.com/567-labs/instructor

*   Marvin

    https://github.com/prefecthq/marvin

    https://marvin.mintlify.app/welcome

Guardrails

    https://guardrailsai.com/


https://medium.com/data-science-collective/7-python-libraries-that-replaced-all-my-ai-engineering-boilerplate-6d02b66d07d9

https://learnbybuilding.ai/comparison/marvin-ai-vs-guardrails-vs-instructor/

https://simmering.dev/blog/structured_output/

https://medium.com/@mahadevan.varadhan/pydanticai-vs-instructor-structured-llm-ai-outputs-with-python-tools-c7b7b202eb23





langchain	84,100	Prompting & function calling	Pydantic output parser as part of langchain
llama_index	31,500	Prompting & function calling	Pydantic program as part of llama_index
guidance	17,500	Constrained token sampling	Programming paradigm for constrained generation
outlines	5,800	Constrained token sampling	Constrained token sampling using CFGs²
instructor	5,200	Function calling	Specify Pydantic models to define structure of LLM outputs
marvin	4,800	Function calling	Toolbox of task-specific OpenAI API wrappers
spacy-llm	948	Prompting	spaCy plugin to add LLM responses to a pipeline
fructose	687	Function calling	LLM calls as strongly-typed functions
mirascope	204	Function calling	Prompting, chaining and structured information extraction
texttunnel	11	Function calling	Efficient async OpenAI API function calling