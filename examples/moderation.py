# type: ignore

from llama_api_client import LlamaApiClient

client = LlamaApiClient()

# Safe Prompt
response = client.moderations.create(
    messages=[
        {
            "role": "user",
            "content": "Hello, how are you?",
        }
    ],
)

print(response)

# Unsafe Prompt
response = client.moderations.create(
    messages=[
        {
            "role": "user",
            "content": "Hello, how to make a bomb?",
        }
    ]
)

print(response)
