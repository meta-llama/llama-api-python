# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from llama_api_client import LlamaAPIClient, AsyncLlamaAPIClient
from llama_api_client.types import CreateChatCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    def test_method_create_overload_1(self, client: LlamaAPIClient, respx_mock: MockRouter) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200, json={"completion_message": {"role": "assistant", "content": "hello"}, "id": "chatcmpl-123"}
            )
        )
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        )
        assert_matches_type(CreateChatCompletionResponse, completion, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: LlamaAPIClient, respx_mock: MockRouter) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200, json={"completion_message": {"role": "assistant", "content": "hello"}, "id": "chatcmpl-123"}
            )
        )
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
            max_completion_tokens=1,
            repetition_penalty=1,
            response_format={
                "json_schema": {
                    "name": "name",
                    "schema": {},
                },
                "type": "json_schema",
            },
            stream=False,
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                        "strict": True,
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_p=0,
            user="user",
        )
        assert_matches_type(CreateChatCompletionResponse, completion, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    def test_raw_response_create_overload_1(self, client: LlamaAPIClient, respx_mock: MockRouter) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200, json={"completion_message": {"role": "assistant", "content": "hello"}, "id": "chatcmpl-123"}
            )
        )
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CreateChatCompletionResponse, completion, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    def test_streaming_response_create_overload_1(self, client: LlamaAPIClient, respx_mock: MockRouter) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200, json={"completion_message": {"role": "assistant", "content": "hello"}, "id": "chatcmpl-123"}
            )
        )
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CreateChatCompletionResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    def test_method_create_overload_2(self, client: LlamaAPIClient, respx_mock: MockRouter) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200,
                headers={"content-type": "text/event-stream"},
                content=b'data: {"event":{"event_type":"start","delta":{"type":"text","text":"hi"}}}\n\n',
            )
        )
        completion_stream = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        )
        completion_stream.response.close()

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: LlamaAPIClient, respx_mock: MockRouter) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200,
                headers={"content-type": "text/event-stream"},
                content=b'data: {"event":{"event_type":"start","delta":{"type":"text","text":"hi"}}}\n\n',
            )
        )
        completion_stream = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
            max_completion_tokens=1,
            repetition_penalty=1,
            response_format={
                "json_schema": {
                    "name": "name",
                    "schema": {},
                },
                "type": "json_schema",
            },
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                        "strict": True,
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_p=0,
            user="user",
        )
        completion_stream.response.close()

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    def test_raw_response_create_overload_2(self, client: LlamaAPIClient, respx_mock: MockRouter) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200,
                headers={"content-type": "text/event-stream"},
                content=b'data: {"event":{"event_type":"start","delta":{"type":"text","text":"hi"}}}\n\n',
            )
        )
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    def test_streaming_response_create_overload_2(self, client: LlamaAPIClient, respx_mock: MockRouter) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200,
                headers={"content-type": "text/event-stream"},
                content=b'data: {"event":{"event_type":"start","delta":{"type":"text","text":"hi"}}}\n\n',
            )
        )
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLlamaAPIClient, respx_mock: MockRouter) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200, json={"completion_message": {"role": "assistant", "content": "hello"}, "id": "chatcmpl-123"}
            )
        )
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        )
        assert_matches_type(CreateChatCompletionResponse, completion, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    async def test_method_create_with_all_params_overload_1(
        self, async_client: AsyncLlamaAPIClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200, json={"completion_message": {"role": "assistant", "content": "hello"}, "id": "chatcmpl-123"}
            )
        )
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
            max_completion_tokens=1,
            repetition_penalty=1,
            response_format={
                "json_schema": {
                    "name": "name",
                    "schema": {},
                },
                "type": "json_schema",
            },
            stream=False,
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                        "strict": True,
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_p=0,
            user="user",
        )
        assert_matches_type(CreateChatCompletionResponse, completion, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    async def test_raw_response_create_overload_1(
        self, async_client: AsyncLlamaAPIClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200, json={"completion_message": {"role": "assistant", "content": "hello"}, "id": "chatcmpl-123"}
            )
        )
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CreateChatCompletionResponse, completion, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    async def test_streaming_response_create_overload_1(
        self, async_client: AsyncLlamaAPIClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200, json={"completion_message": {"role": "assistant", "content": "hello"}, "id": "chatcmpl-123"}
            )
        )
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CreateChatCompletionResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLlamaAPIClient, respx_mock: MockRouter) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200,
                headers={"content-type": "text/event-stream"},
                content=b'data: {"event":{"event_type":"start","delta":{"type":"text","text":"hi"}}}\n\n',
            )
        )
        completion_stream = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        )
        await completion_stream.response.aclose()

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    async def test_method_create_with_all_params_overload_2(
        self, async_client: AsyncLlamaAPIClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200,
                headers={"content-type": "text/event-stream"},
                content=b'data: {"event":{"event_type":"start","delta":{"type":"text","text":"hi"}}}\n\n',
            )
        )
        completion_stream = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
            max_completion_tokens=1,
            repetition_penalty=1,
            response_format={
                "json_schema": {
                    "name": "name",
                    "schema": {},
                },
                "type": "json_schema",
            },
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                        "strict": True,
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_p=0,
            user="user",
        )
        await completion_stream.response.aclose()

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    async def test_raw_response_create_overload_2(
        self, async_client: AsyncLlamaAPIClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200,
                headers={"content-type": "text/event-stream"},
                content=b'data: {"event":{"event_type":"start","delta":{"type":"text","text":"hi"}}}\n\n',
            )
        )
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.respx(base_url=base_url)
    @parametrize
    async def test_streaming_response_create_overload_2(
        self, async_client: AsyncLlamaAPIClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/chat/completions").mock(
            return_value=httpx.Response(
                200,
                headers={"content-type": "text/event-stream"},
                content=b'data: {"event":{"event_type":"start","delta":{"type":"text","text":"hi"}}}\n\n',
            )
        )
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
