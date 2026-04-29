"""
Prompt templates and tool descriptions for the research deepagent.
"""

f = open("./agents/agent_deep_research/research-workflow.instructions.md", "r")
RESEARCH_WORKFLOW_INSTRUCTIONS = f.read()

f = open("./agents/agent_deep_research/researcher.instructions.md", "r")
RESEARCHER_INSTRUCTIONS = f.read()

f = open("./agents/agent_deep_research/task-description-prefix.md", "r")
TASK_DESCRIPTION_PREFIX = f.read()

f = open("./agents/agent_deep_research/research-workflow.instructions.md", "r")
SUBAGENT_DELEGATION_INSTRUCTIONS = f.read()
