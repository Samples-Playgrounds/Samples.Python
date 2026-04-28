# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Required environment variables:
- `TAVILY_API_KEY` — for web search via Tavily
- Anthropic API key (standard `ANTHROPIC_API_KEY`) for `init_chat_model`

## Running

```shell
python main.py        # run the agent entrypoint
```

To reset the environment:
```shell
deactivate
rm -fr .venv/ __pycache__/
```

## Architecture

This is a **deep research agent** built on `deepagents` + LangGraph/LangChain.

### Entry points

- `main.py` — legacy scratch file with inline tool definitions (kept for reference; not the canonical module)
- `agent.py` — canonical agent construction: imports from `agents/agent_deep_research/`, wires up the orchestrator + sub-agent, and exposes the `agent` object for LangGraph deployment

### Core module: `agents/agent_deep_research/`

| File | Role |
|------|------|
| `tools.py` | Two LangChain tools: `tavily_search` (Tavily URL discovery → full page fetch → markdown) and `think_tool` (structured reflection step between searches) |
| `prompts.py` | Three prompt strings: `RESEARCH_WORKFLOW_INSTRUCTIONS` (orchestrator workflow), `RESEARCHER_INSTRUCTIONS` (sub-agent loop with hard search limits), `SUBAGENT_DELEGATION_INSTRUCTIONS` (parallelization strategy) |

### Agent topology

```
Orchestrator (claude-sonnet-4-5)
  ├── tools: tavily_search, think_tool
  ├── prompt: RESEARCH_WORKFLOW_INSTRUCTIONS + SUBAGENT_DELEGATION_INSTRUCTIONS
  └── subagent: "research-agent"
        ├── tools: tavily_search, think_tool
        └── prompt: RESEARCHER_INSTRUCTIONS
```

The orchestrator delegates research topics to sub-agents (up to 3 in parallel, up to 3 delegation rounds). Sub-agents run their own search loop (2–5 calls max), then return structured findings with inline citations. The orchestrator consolidates all citations into a final `/final_report.md`.

### Key design decisions

- `TavilyClient()` in `tools.py` reads `TAVILY_API_KEY` from the environment automatically (no explicit `api_key` arg).
- `think_tool` is a no-op that returns its input — its value is forcing the LLM to emit a structured reflection between tool calls, improving research quality.
- The model is set to `anthropic:claude-sonnet-4-5-20250929` in `agent.py`; a commented-out Gemini alternative is also present.
