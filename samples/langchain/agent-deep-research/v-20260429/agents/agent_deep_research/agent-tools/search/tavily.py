"""
Research Tools.

Search.tavily

This module provides search and content processing utilities for the research agent,
using Tavily for URL discovery and fetching full webpage content.
"""

from langchain_core.tools import InjectedToolArg, tool
from tavily import TavilyClient

@tool(parse_docstring=True)
def tavily_search(
                    query: str,
                    max_results: 
                                Annotated[int, InjectedToolArg] = 1,
                    topic:
                                Annotated[
                                            Literal["general", "news", "finance"], 
                                            InjectedToolArg
                                        ] = "general",
                ) -> str:
    """
    Search the web for information on a given query.

    Uses Tavily to discover relevant URLs, then fetches and returns full webpage content as markdown.

    Args:
        query: Search query to execute
        max_results: Maximum number of results to return (default: 1)
        topic: Topic filter - 'general', 'news', or 'finance' (default: 'general')

    Returns:
        Formatted search results with full webpage content
    """
    # Use Tavily to discover URLs
    search_results = tavily_client.search(
        query,
        max_results=max_results,
        topic=topic,
    )

    # Fetch full content for each URL
    result_texts = []
    for result in search_results.get("results", []):
        url = result["url"]
        title = result["title"]

        # Fetch webpage content
        content = fetch_webpage_content(url)

        result_text = 
        f"""
        ## {title}

        **URL:** {url}

        {content}

        ---
        """
        result_texts.append(result_text)

    # Format final response
    response = 
    f"""
    🔍 Found {len(result_texts)} result(s) for '{query}':

    {chr(10).join(result_texts)}
    """

    return response
