# type: ignore

import json

from llama_api_client import LlamaAPIClient

client = LlamaAPIClient()

MODEL = "Llama-4-Maverick-17B-128E-Instruct-FP8"


def get_weather(location: str) -> str:
    return f"The weather in {location} is sunny."


def run(stream: bool = False) -> None:
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get current weather for a given location.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City and country e.g. Bogotá, Colombia",
                        }
                    },
                    "required": ["location"],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        }
    ]
    messages = [
        {"role": "user", "content": "Is it raining in Bellevue?"},
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        max_completion_tokens=2048,
        temperature=0.6,
        stream=stream,
    )

    completion_message = None
    if stream:
        tool_call = {"function": {"arguments": ""}}

        stop_reason = None
        for chunk in response:
            if chunk.event.delta.type == "tool_call":
                if chunk.event.delta.id:
                    tool_call["id"] = chunk.event.delta.id
                if chunk.event.delta.function.name:
                    print(
                        f"Using tool_id={chunk.event.delta.id} with name={chunk.event.delta.function.name}",
                    )
                    tool_call["function"]["name"] = chunk.event.delta.function.name
                if chunk.event.delta.function.arguments:
                    tool_call["function"][
                        "arguments"
                    ] += chunk.event.delta.function.arguments
                    print(chunk.event.delta.function.arguments, end="", flush=True)

            if chunk.event.stop_reason is not None:
                stop_reason = chunk.event.stop_reason

        completion_message = {
            "role": "assistant",
            "content": {
                "type": "text",
                "text": "",
            },
            "tool_calls": [tool_call],
            "stop_reason": stop_reason,
        }
    else:
        print(response)
        completion_message = response.completion_message.model_dump()

    # Next Turn
    messages.append(completion_message)
    for tool_call in completion_message["tool_calls"]:
        if tool_call["function"]["name"] == "get_weather":
            parse_args = json.loads(tool_call["function"]["arguments"])
            result = get_weather(**parse_args)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "content": result,
                },
            )

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        max_completion_tokens=2048,
        temperature=0.6,
        stream=stream,
    )

    if stream:
        for chunk in response:
            print(chunk.event.delta.text, end="", flush=True)
    else:
        print(response)


if __name__ == "__main__":
    run(stream=True)
    run(stream=False)
