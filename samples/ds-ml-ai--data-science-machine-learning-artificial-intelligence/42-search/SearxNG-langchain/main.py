"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

pip install langchain 
pip install langchain-community

pip install orjson
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""


from langchain_community.utilities import SearxSearchWrapper
import pprint

s = SearxSearchWrapper(searx_host="http://localhost:8080",)
result = s.results(
                    "What is .NET Aspire?", 
                    num_results=10, 
                    engines=[
                                "google"
                            ]
                )
pprint.pprint(result)

## Github Tool

from langchain_community.tools.searx_search.tool import SearxSearchResults

wrapper = SearxSearchWrapper(searx_host="**")
github_tool = SearxSearchResults(name="Github", wrapper=wrapper,
                            kwargs = {
                                "engines": ["github"],
                                })
