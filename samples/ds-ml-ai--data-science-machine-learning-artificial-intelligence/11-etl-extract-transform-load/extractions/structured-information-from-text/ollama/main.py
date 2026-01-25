from ollama import chat
from ollama import ChatResponse

files = [
    f"/Users/Shared/Projects/e/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf",
]



def main():


   for file in files:
      print(f"ollama <- file = {file}")

        text = ""
        
        with open(f"{source}", 'r') as file:
            text = file.read()

        prompt = """
        Extract data from text:
        {text}
        """


    response: ChatResponse = chat(model='gemma3:27b', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)




if __name__ == '__main__':
    main()

