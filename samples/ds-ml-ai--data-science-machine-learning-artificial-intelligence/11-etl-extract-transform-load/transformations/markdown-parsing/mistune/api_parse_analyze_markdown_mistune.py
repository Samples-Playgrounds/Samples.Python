import mistune
from typing import Union

import json
from pathlib import Path

import traceback
import datetime
import time
from time import perf_counter
from time import perf_counter_ns


def api_parse_analyze_markdown_mistune(source: str) -> Union[str, None]:
    """
    Parse markdown documents using mistune.

    Setup:
        python -m venv .venv
        source .venv/bin/activate
        pip install mistune

    Usage:
        python main.py
    """
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()

    directory = f"{source}.hwaifs/parse-analysis/py/mistune/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    try:
        with open(source, "r") as f:
            markdown_text = f.read()

        markdown_ast = mistune.create_markdown(renderer="ast")
        ast = markdown_ast(markdown_text)

        html_renderer = mistune.create_markdown(renderer="html")
        html = html_renderer(markdown_text)

        tokens = ast

        output_tokens = {
            "result": tokens,
            "metadata": {
                "parser": "mistune",
                "source": source,
                "ast_type": "list",
                "element_count": len(tokens) if isinstance(tokens, list) else 1,
            },
        }

        Path(directory).mkdir(parents=True, exist_ok=True)

        with open(f"{directory}/tokens.json", "w") as f:
            json.dump(output_tokens, f, indent=4, default=str)

        with open(f"{directory}/content.html", "w") as f:
            f.write(html)

    except Exception as e:
        tb = traceback.format_exc()
        msg = (
            f"Exception parsing markdown with mistune = {source} : {e}"
            + tb
        )
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)

        return

    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name": "api_parse_analyze_markdown_mistune",
        "time_start_1": time_start_1,
        "time_end_1": time_stop_1,
        "time_total_1": time_total_1,
        "time_start_2": time_start_2,
        "time_end_2": time_stop_2,
        "time_total_2": time_total_2,
        "time_start_3": time_start_3,
        "time_end_3": time_stop_3,
        "time_total_3": time_total_3,
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.py.json", "w") as f:
        f.write(json.dumps(times, indent=4))

    return json.dumps(output_tokens, indent=4, default=str)