# type: ignore

from llama_api import LlamaAPI

client = LlamaAPI()

# Non-Streaming
response = client.chat.completions.create(
    model="Llama-3.3-70B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Hello, how are you?",
        }
    ],
    max_completion_tokens=1024,
    temperature=0.7,
)

print(response)

# Streaming the next response
response = client.chat.completions.create(
    model="Llama-3.3-70B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Hello, how are you?",
        },
        response.completion_message,
        {
            "role": "user",
            "content": "Hello again",
        },
    ],
    max_completion_tokens=1024,
    temperature=0.7,
    stream=True,
)

for chunk in response:
    print(chunk.event.delta.text, end="", flush=True)
