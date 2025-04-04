# type: ignore

import base64
import os

from llama_api import LlamaAPI

client = LlamaAPI()


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def run(stream: bool = False) -> None:
    encoded_image = encode_image(os.path.join(os.path.dirname(__file__), "logo.png"))

    response = client.chat.completions.create(
        model="Llama-4-17B-128E-Omni",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is in this image?",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encoded_image}",
                        },
                    },
                ],
            },
        ],
        stream=stream,
    )

    if stream:
        for chunk in response:
            print(chunk.event.delta.text, end="", flush=True)
    else:
        print(response)


if __name__ == "__main__":
    run(stream=False)
    run(stream=True)
