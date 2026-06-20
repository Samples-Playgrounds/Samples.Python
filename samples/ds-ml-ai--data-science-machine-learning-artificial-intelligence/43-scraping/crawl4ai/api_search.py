import asyncio
from crawl4ai import *

# https://docs.crawl4ai.com/core/examples/

async def search_site   (
                            site_url : str
                        ) -> str:
    """
    """
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
                                        url=site_url
                                 )
        
    return result.markdown
    