from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin


from pathlib import Path

def api_parse_analyze_markdown_markdown_it_py (source: str) -> str:
    """
    """


    directory = f"{source}.hwaifs/parse-analysis/py/mrkdwn_analysis/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    md = (
        MarkdownIt('commonmark', 
        {'breaks':True, 'html':True})
        .use(front_matter_plugin)
        .use(footnote_plugin)
        .enable('table')
    )
    with open(source, 'r') as f:
        text = f.read()

    tokens = md.parse(text)

    return tokens