import re import requests 

from bs4 import BeautifulSoup 
from urllib.parse import urljoin

LIBRARY_URL = "https://ollama.com/library/" 
MANIFEST_URL = "https://registry.ollama.ai/v2/library/{name}/manifests/{tag}" 
OUTPUT_FILE = "ollama_models_ranked_by_vram.txt"

HEADERS = { 
            "User-Agent": "ollama-vram-ranker/1.1" 
        }

WEIGHT_MEDIA_TYPES = { 
                        "application/vnd.ollama.image.model", 
                        "application/vnd.ollama.image.projector", 
                        # vision models 
                    }

session = requests.Session() session.headers.update(HEADERS) 