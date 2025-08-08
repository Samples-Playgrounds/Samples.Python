# python3.13 -m venv .venv
# source .venv/bin/activate
# pip3.13 install "llama_index"
# pip3.13 freeze > requirements.txt

import api

text = """
One of the most important things I didn't understand about the world when I was a child is the degree to which the returns for performance are superlinear.

Teachers and coaches implicitly told us the returns were linear. "You get out," I heard a thousand times, "what you put in." They meant well, but this is rarely true. If your product is only half as good as your competitor's, you don't get half as many customers. You get no customers, and you go out of business.

It's obviously true that the returns for performance are superlinear in business. Some think this is a flaw of capitalism, and that if we changed the rules it would stop being true. But superlinear returns for performance are a feature of the world, not an artifact of rules we've invented. We see the same pattern in fame, power, military victories, knowledge, and even benefit to humanity. In all of these, the rich get richer. [1]
"""

documents = api.split_text(text, 65, 0)

for document in documents:
   print(f"============================================================================")
   print(document)

documents = api.split_text(text, 450, 0)

for document in documents:
   print(f"============================================================================")
   print(document)
