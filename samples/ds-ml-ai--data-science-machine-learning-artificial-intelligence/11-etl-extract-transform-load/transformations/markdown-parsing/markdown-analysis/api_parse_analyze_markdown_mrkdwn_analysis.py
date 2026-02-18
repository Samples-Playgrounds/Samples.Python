from mrkdwn_analysis import MarkdownAnalyzer


from pathlib import Path

def api_parse_analyze_markdown_mrkdwn_analysis (source: str) -> str:
    """
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/parse-analysis/py/mrkdwn_analysis/"
    Path(directory).mkdir(parents=True, exist_ok=True)

    analyzer = MarkdownAnalyzer(source)

    result = ""
    json = ""

    try:
        print(f"analyzer.identify_headers()")
        headers = analyzer.identify_headers()
        with open(f"{directory}/headers.json", "w") as f:
            json = str(headers)
            result += f"headers = {json}\n\n"
            f.write(json)
        
        print(f"analyzer.identify_paragraphs()")
        paragraphs = analyzer.identify_paragraphs()
        with open(f"{directory}/paragraphs.json", "w") as f:
            json = str(paragraphs)
            result += f"paragraphs = {json}\n\n"
            f.write(json)

        print(f"analyzer.identify_tables()")
        tables = analyzer.identify_tables()
        with open(f"{directory}/tables.json", "w") as f:
            json = str(tables)
            result += f"tables = {json}\n\n"
            f.write(json)

        print(f"analyzer.identify_links()")
        links = analyzer.identify_links()
        with open(f"{directory}/links.json", "w") as f:
            json = str(links)
            result += f"links = {json}\n\n"
            f.write(json)

        print(f"analyzer.identify_lists()")
        lists = analyzer.identify_lists()
        with open(f"{directory}/lists.json", "w") as f:
            json = str(lists)
            result += f"lists = {json}\n\n"
            f.write(json)

        print(f"analyzer.identify_code_blocks()")
        code_blocks = analyzer.identify_code_blocks()
        with open(f"{directory}/code_blocks.json", "w") as f:
            json = str(code_blocks)
            result += f"code_blocks = {json}\n\n"
            f.write(json)

        print(f"analyzer.identify_html_blocks()")
        html_blocks = analyzer.identify_html_blocks()
        with open(f"{directory}/html_blocks.json", "w") as f:
            json = str(html_blocks)
            result += f"html_blocks = {json}\n\n"
            f.write(json)

        print(f"analyzer.identify_html_inline()")
        html_inline = analyzer.identify_html_inline()
        with open(f"{directory}/html_inline.json", "w") as f:
            json = str(html_inline)
            result += f"html_inline = {json}\n\n"
            f.write(json)
    except Exception as e:
        tb = traceback.format_exc()
        msg = \
            f"Exception reading tables from PDF document source = {source} : {e}" \
            + \
            tb
        timestamp = datetime.datetime.now().isoformat().replace(":", "-")
        with open(f"{directory}/exception-{timestamp}.py.json", "w") as f:
            f.write(msg)
        
        return

    #---------------------------------------------------------------------------
    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name" : "extract_text_to_file_from_any_document",
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
    #---------------------------------------------------------------------------

    return result