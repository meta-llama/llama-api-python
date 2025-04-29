# type: ignore

import asyncio

from llama_api_client import AsyncLlamaAPIClient

client = AsyncLlamaAPIClient()


async def main() -> None:
    response = await client.chat.completions.create(
        model="Llama-3.3-70B-Instruct",
        messages=[{"role": "user", "content": "Hello"}],
        stream=True,
    )
    async for chunk in response:
        print(chunk.event.delta.text, end="", flush=True)

    print()


asyncio.run(main())
