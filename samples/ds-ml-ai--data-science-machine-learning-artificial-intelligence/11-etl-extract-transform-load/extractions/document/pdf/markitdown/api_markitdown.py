from markitdown import MarkItDown

def covert_file_to_markdown (source: str) -> str:
    md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
    result_md = md.convert(source)

    return result_md.text_content
