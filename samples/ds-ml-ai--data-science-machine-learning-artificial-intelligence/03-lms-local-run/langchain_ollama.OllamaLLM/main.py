"""
# ollama run gpt-oss:20b
ollama run llama3.3:latest

rm -fr .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip3.13 install "langchain-ollama"
pip3.13 freeze > requirements.txt
"""

# import api

# document per local path or URL
#file="mit.txt"

#  "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#   "https://arxiv.org/pdf/2408.09869"

print(f"============================================================================")
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.3:latest")

#    raise mapped_exc(message) from exc
# httpx.ConnectError: [Errno 61] Connection refused

# ollama run llama3.3:latest 
response = llm.invoke("The first man on the moon was ...")

print(f"response = {response}")


print(f"============================================================================")
from langchain_ollama import ChatOllama

chat_model = ChatOllama(model="llama3.3:latest")

response = chat_model.invoke("Who was the first man on the moon?")

print(f"response = {response}")
