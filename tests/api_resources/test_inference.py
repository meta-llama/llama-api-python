# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_api import LlamaAPI, AsyncLlamaAPI
from tests.utils import assert_matches_type
from llama_api.types import InferenceGenerateChatCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInference:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_chat_completion(self, client: LlamaAPI) -> None:
        inference = client.inference.generate_chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model_id="model_id",
        )
        assert_matches_type(InferenceGenerateChatCompletionResponse, inference, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_chat_completion_with_all_params(self, client: LlamaAPI) -> None:
        inference = client.inference.generate_chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                }
            ],
            model_id="model_id",
            logprobs={"top_k": 0},
            response_format={
                "json_schema": {"foo": True},
                "type": "json_schema",
            },
            sampling_params={
                "strategy": {"type": "greedy"},
                "max_tokens": 0,
                "repetition_penalty": 0,
            },
            stream=True,
            tool_choice="auto",
            tool_config={
                "system_message_behavior": "append",
                "tool_choice": "auto",
                "tool_prompt_format": "json",
            },
            tool_prompt_format="json",
            tools=[
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                }
            ],
        )
        assert_matches_type(InferenceGenerateChatCompletionResponse, inference, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_generate_chat_completion(self, client: LlamaAPI) -> None:
        response = client.inference.with_raw_response.generate_chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model_id="model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = response.parse()
        assert_matches_type(InferenceGenerateChatCompletionResponse, inference, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_generate_chat_completion(self, client: LlamaAPI) -> None:
        with client.inference.with_streaming_response.generate_chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model_id="model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = response.parse()
            assert_matches_type(InferenceGenerateChatCompletionResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInference:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_chat_completion(self, async_client: AsyncLlamaAPI) -> None:
        inference = await async_client.inference.generate_chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model_id="model_id",
        )
        assert_matches_type(InferenceGenerateChatCompletionResponse, inference, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_chat_completion_with_all_params(self, async_client: AsyncLlamaAPI) -> None:
        inference = await async_client.inference.generate_chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                }
            ],
            model_id="model_id",
            logprobs={"top_k": 0},
            response_format={
                "json_schema": {"foo": True},
                "type": "json_schema",
            },
            sampling_params={
                "strategy": {"type": "greedy"},
                "max_tokens": 0,
                "repetition_penalty": 0,
            },
            stream=True,
            tool_choice="auto",
            tool_config={
                "system_message_behavior": "append",
                "tool_choice": "auto",
                "tool_prompt_format": "json",
            },
            tool_prompt_format="json",
            tools=[
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                }
            ],
        )
        assert_matches_type(InferenceGenerateChatCompletionResponse, inference, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_generate_chat_completion(self, async_client: AsyncLlamaAPI) -> None:
        response = await async_client.inference.with_raw_response.generate_chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model_id="model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = await response.parse()
        assert_matches_type(InferenceGenerateChatCompletionResponse, inference, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_generate_chat_completion(self, async_client: AsyncLlamaAPI) -> None:
        async with async_client.inference.with_streaming_response.generate_chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
            model_id="model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = await response.parse()
            assert_matches_type(InferenceGenerateChatCompletionResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True
