# type: ignore

from llama_api import LlamaAPI

client = LlamaAPI()


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
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Is it raining in Bellevue?"},
    ]

    response = client.chat.completions.create(
        model="Llama-3.3-70B-Instruct",
        messages=messages,
        tools=tools,
        max_completion_tokens=2048,
        temperature=0.9,
        stream=stream,
    )

    completion_message = None
    if stream:
        tool_call = {"function": {"arguments": ""}}
        for chunk in response:
            stop_reason = None
            if chunk.event.delta.type == "tool_call":
                if chunk.event.delta.id:
                    tool_call["id"] = chunk.event.delta.id
                if chunk.event.delta.function.name:
                    print(
                        f"Using tool_id={chunk.event.delta.id} with name={chunk.event.delta.function.name}",
                    )
                    tool_call["function"]["name"] = chunk.event.delta.function.name
                elif chunk.event.delta.function.arguments:
                    tool_call["function"][
                        "arguments"
                    ] += chunk.event.delta.function.arguments
                    print(chunk.event.delta.function.arguments, end="", flush=True)

            if chunk.event.stop_reason:
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
    messages.append(
        {
            "role": "tool",
            "tool_call_id": completion_message["tool_calls"][0]["id"],
            "content": "raining",
        },
    )

    response = client.chat.completions.create(
        model="Llama-3.3-70B-Instruct",
        messages=messages,
        tools=tools,
        max_completion_tokens=2048,
        temperature=0.9,
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
