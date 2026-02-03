 def get_html(url): 
    r = session.get(url, timeout=30) 
    r.raise_for_status() 
    return r.text

def bytes_to_gb(b): 
    return b / (1024 ** 3)
