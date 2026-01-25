import ollama

response = ollama.chat(
    model="llama3.2-vision:latest",
    messages=[
        {
            "role": "user",
            "content": "Describe the image",
            "images": 
                    [
                        "./cat.jpeg"
                    ]
        }
    ],
)

print(response["message"]['role'])
print(response["message"]['content'])
