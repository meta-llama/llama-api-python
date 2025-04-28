# type: ignore

import os
import base64

from llama_api_client import LlamaAPIClient

client = LlamaAPIClient()


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def run(stream: bool = False) -> None:
    encoded_image = encode_image(os.path.join(os.path.dirname(__file__), "logo.png"))
    encoded_image2 = encode_image(os.path.join(os.path.dirname(__file__), "logo2.png"))

    response = client.chat.completions.create(
        model="Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is different about these two images?",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encoded_image}",
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encoded_image2}",
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
