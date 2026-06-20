"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate

pip install crawl4ai
# Setup the browser
crawl4ai-setup

pip install orjson
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_search as api

import sys
import os
scriptpath = "../../"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
from data import *

def main():
    sites_urls = [
                    "https://aspire.dev/docs/",
                    "https://learn.microsoft.com/en-us/dotnet/maui/",
                    "https://learn.microsoft.com/en-us/dotnet/",
                    "https://learn.microsoft.com/en-us/aspnet/core/",
                    "https://learn.microsoft.com/en-us/azure/",
                    "https://learn.microsoft.com/en-us/dotnet/csharp/",
                 ]

# async def main():
#     site_url = 'https://aspire.dev/docs/'
#     async with AsyncWebCrawler() as crawler:
#         result = await crawler.arun(
#                                         url=site_url
#                                     )
#         print(result.markdown)

if __name__ == '__main__':
    
    main()
    # asyncio.run(main())
