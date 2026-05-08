"""
Research Agent - Standalone script for LangGraph deployment.

This module creates a deep research agent with custom tools and prompts
for conducting web research with strategic thinking and context management.
"""

import stringcase
from datetime import datetime

from langchain.chat_models import init_chat_model
from deepagents import create_deep_agent

from agents.agent_deep_research.prompts import (
                                                    RESEARCHER_INSTRUCTIONS,
                                                    RESEARCH_WORKFLOW_INSTRUCTIONS,
                                                    SUBAGENT_DELEGATION_INSTRUCTIONS,
                                                )

# Limits
max_concurrent_research_units = 3
max_researcher_iterations = 3

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Combine orchestrator instructions (RESEARCHER_INSTRUCTIONS only for sub-agents)
INSTRUCTIONS = (
    RESEARCH_WORKFLOW_INSTRUCTIONS
    + "\n\n"
    + "=" * 80
    + "\n\n"
    + SUBAGENT_DELEGATION_INSTRUCTIONS.format(
        max_concurrent_research_units=max_concurrent_research_units,
        max_researcher_iterations=max_researcher_iterations,
    )
)

from agents.agent_deep_research.agent_tools.search.tavily import tavily_search
from agents.agent_deep_research.agent_tools.think_tool import think_tool

# Create research sub-agent
research_sub_agent = \
{
    "name": "research-agent",
    "description": "Delegate research to the sub-agent researcher. Only give this researcher one topic at a time.",
    "system_prompt": RESEARCHER_INSTRUCTIONS.format(date=current_date),
    "tools":
            [
                tavily_search,
                think_tool
            ],
}


def research_topics(
                        topics: str[],
                        model: str = "anthropic:claude-sonnet-4-5-20250929"
                    ) -> str:
    """
    """
    model = get_model(model)

    # Create the agent
    # https://docs.langchain.com/oss/python/deepagents/cli/providers
    https://github.com/langchain-ai/deepagents
    agent = create_deep_agent(
                                model=model,
                                tools=
                                        [
                                            tavily_search,
                                            think_tool
                                        ],
                                system_prompt=INSTRUCTIONS,
                                subagents=
                                            [
                                                research_sub_agent
                                            ],
                            )

    for topic in topics:
        print("researching topic:", topic)

        result = agent.invoke(
                                {
                                    "messages": 
                                    [
                                        {
                                            "role": "user",
                                            "content": f"{topic}",
                                        }
                                    ],
                                }, 
                            )

        for msg in result["messages"]:
            role = getattr(msg, "type", msg.__class__.__name__)
            content = getattr(msg, "content", str(msg))
            txt_content = \
            f"""
            {topic}
            """
            if content:
                txt_content += f"[{role}]: {content}\n"

            print(txt_content)
            txt_topic = stringcase.spinalcase(topic)
            with open(f"research_agent_output--{txt_topic}.txt", "a") as f:
                f.write(txt_content)


def get_model(model_name: str) :
    
    match model_name:
        case "gemini-3-pro-preview":
            # Model Gemini 3 
            model = ChatGoogleGenerativeAI(
                                            model=model_name,
                                            temperature=0.0
                                        )

            return model
        case "anthropic:claude-sonnet-4-5-20250929":
            # Model Claude 4.5
            model = init_chat_model(
                                        model=,
                                        temperature=0.0
                                    )

            return model
        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return "Something's wrong with the internet"
            

