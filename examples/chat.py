# type: ignore

from llama_api_client import LlamaAPIClient

client = LlamaAPIClient()

# Non-Streaming
response = client.chat.completions.create(
    model="Llama-4-Maverick-17B-128E-Instruct-FP8",
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
    model="Llama-4-Maverick-17B-128E-Instruct-FP8",
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
