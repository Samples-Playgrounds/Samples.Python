 def get_all_models                     (    
                                        ):
    """
    Fetch all available models from the Ollama library.
    """   
    
    html = get_html(LIBRARY_URL) 
    soup = BeautifulSoup(html, "html.parser")

    models = set()
    for a in soup.select('a[href^="/library/"]'):
        href = a.get("href", "")
        m = re.fullmatch(r"/library/([^/]+)", href)
        if m:
            models.add(m.group(1))

    return sorted(models)



def get_model_tags                      (
                                            model: str
                                        ):
    """
    Fetch available tags for a given model.
    """

    url = urljoin(LIBRARY_URL, model) 
    html = get_html(url) 
    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(" ", strip=True).lower()
    tags = set()

    for token in text.split():
        if re.fullmatch(r"\d+(\.\d+)?b", token):
            tags.add(token)
        elif token == "latest":
            tags.add(token)

    if not tags:
        tags.add("latest")

    # latest first, then numeric
    def sort_key(t):
        if t == "latest":
            return (0, 0)
        m = re.match(r"(\d+(\.\d+)?)b", t)
        return (1, float(m.group(1)) if m else 999)

    return sorted(tags, key=sort_key)