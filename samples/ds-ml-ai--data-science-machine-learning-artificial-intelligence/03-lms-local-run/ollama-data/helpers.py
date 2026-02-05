 def get_html(url): 
    """
    Fetch HTML content from a URL with error handling.
    """

    r = session.get(url, timeout=30) 
    r.raise_for_status() 
    return r.text

def bytes_to_gb(b): 
    """
    Convert bytes to gigabytes.
    """
        
    return b / (1024 ** 3)
