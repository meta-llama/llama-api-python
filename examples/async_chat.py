import asyncio

from llama_api import AsyncLlamaAPI

client = AsyncLlamaAPI()


async def main() -> None:
    stream = await client.chat.completions.create(
        model="Llama-3.3-70B-Instruct",
        messages=[{"role": "user", "content": "Hello"}],
        stream=True,
    )
    async for chunk in stream:
        assert chunk.event.delta.type == "text"
        print(chunk.event.delta.text, end="", flush=True)

    print()


asyncio.run(main())
