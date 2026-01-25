"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install langchain
pip install langchain-core
pip install langchain-community
pip install langchain-classic
pip install langchain_classic
pip install langchain-ollama
pip install ollama
pip install openai

pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

# https://ollama.com/blog/how-to-prompt-code-llama

from langchain_community.llms import Ollama
from langchain_classic.chains import LLMChain
from langchain_classic.prompts import PromptTemplate

llm = Ollama(model = "llama3.3:latest")
template = PromptTemplate(
                            input_variables=["code"],
                            template="Detect programing language and explain code in {code}"
                        )
code = """
        using System;
        public class Test
        {
            static int Fib(int n) {
                return (n < 2)? n : Fib(n - 1) + Fib(n - 2);
            }
            public static void Main()
            {
                Console.Write(Fib(10));
            }
        }
        """

chain = LLMChain(llm=llm, prompt=template)
explanation = chain.invoke(code=code

print(explanation)