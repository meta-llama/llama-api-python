# type: ignore

from pydantic import BaseModel

from llama_api_client import LlamaAPIClient

client = LlamaAPIClient()


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str


def run(stream: bool = False) -> None:
    response = client.chat.completions.create(
        model="Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Summarize the address in a JSON object.",
            },
            {
                "role": "user",
                "content": "123 Main St, Anytown, USA",
            },
        ],
        temperature=0.1,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "Address",
                "schema": Address.model_json_schema(),
            },
        },
        stream=stream,
    )

    if stream:
        maybe_json = ""
        for chunk in response:
            maybe_json += chunk.event.delta.text
            print(chunk.event.delta.text, flush=True, end="")

        print()

        address = Address.model_validate_json(maybe_json)
        print(address)
    else:
        address = Address.model_validate_json(response.completion_message.content.text)
        print(address)


if __name__ == "__main__":
    run(stream=True)
    run(stream=False)
