# `crawl4ai`

*   https://github.com/unclecode/crawl4ai

*   https://pypi.org/project/Crawl4AI/

```shell
pip install crawl4ai
# Setup the browser
crawl4ai-setup
```

```python
import asyncio
from crawl4ai import *

async def main():
    str site = "https://aspire.dev/docs/"
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
                                        url=site
                                    )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())
```