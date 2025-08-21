import ollama

response = ollama.chat(
    model="moondream",
    messages=[
        {"role": "user", "content": "Describe the image", "images": ["./cat.jpeg"]}
    ],
)

print(response["message"]['role'])
print(response["message"]['content'])
