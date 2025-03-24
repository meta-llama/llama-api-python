# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import inference_chat_completion_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.message_param import MessageParam
from ..types.chat_completion_response import ChatCompletionResponse
from ..types.chat_completion_response_stream_chunk import ChatCompletionResponseStreamChunk

__all__ = ["InferenceResource", "AsyncInferenceResource"]


class InferenceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-api-python#accessing-raw-response-data-eg-headers
        """
        return InferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-api-python#with_streaming_response
        """
        return InferenceResourceWithStreamingResponse(self)

    @overload
    def chat_completion(
        self,
        *,
        messages: Iterable[MessageParam],
        model_id: str,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: inference_chat_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation

          model_id: The identifier of the model to use.

          logprobs: If specified, log probabilities for each token position will be returned.

          response_format: Grammar specification for guided (structured) decoding. There are two options: -
              `ResponseFormat.json_schema`: The grammar is a JSON schema. Most providers
              support this format. - `ResponseFormat.grammar`: The grammar is a BNF grammar.
              This format is more flexible, but not all providers support it.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          tool_choice: Whether tool use is required or automatic. Defaults to ToolChoice.auto. ..
              deprecated:: Use tool_config instead.

          tool_config: Configuration for tool use.

          tool_prompt_format: Instructs the model how to format tool calls. By default, Llama Stack will
              attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: List of tool definitions available to the model

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def chat_completion(
        self,
        *,
        messages: Iterable[MessageParam],
        model_id: str,
        stream: Literal[True],
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: inference_chat_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation

          model_id: The identifier of the model to use.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          logprobs: If specified, log probabilities for each token position will be returned.

          response_format: Grammar specification for guided (structured) decoding. There are two options: -
              `ResponseFormat.json_schema`: The grammar is a JSON schema. Most providers
              support this format. - `ResponseFormat.grammar`: The grammar is a BNF grammar.
              This format is more flexible, but not all providers support it.

          tool_choice: Whether tool use is required or automatic. Defaults to ToolChoice.auto. ..
              deprecated:: Use tool_config instead.

          tool_config: Configuration for tool use.

          tool_prompt_format: Instructs the model how to format tool calls. By default, Llama Stack will
              attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: List of tool definitions available to the model

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def chat_completion(
        self,
        *,
        messages: Iterable[MessageParam],
        model_id: str,
        stream: bool,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: inference_chat_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse | Stream[ChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation

          model_id: The identifier of the model to use.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          logprobs: If specified, log probabilities for each token position will be returned.

          response_format: Grammar specification for guided (structured) decoding. There are two options: -
              `ResponseFormat.json_schema`: The grammar is a JSON schema. Most providers
              support this format. - `ResponseFormat.grammar`: The grammar is a BNF grammar.
              This format is more flexible, but not all providers support it.

          tool_choice: Whether tool use is required or automatic. Defaults to ToolChoice.auto. ..
              deprecated:: Use tool_config instead.

          tool_config: Configuration for tool use.

          tool_prompt_format: Instructs the model how to format tool calls. By default, Llama Stack will
              attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: List of tool definitions available to the model

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model_id"], ["messages", "model_id", "stream"])
    def chat_completion(
        self,
        *,
        messages: Iterable[MessageParam],
        model_id: str,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: inference_chat_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse | Stream[ChatCompletionResponseStreamChunk]:
        return self._post(
            "/v1/inference/chat-completion",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model_id": model_id,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "repetition_penalty": repetition_penalty,
                    "response_format": response_format,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tool_config": tool_config,
                    "tool_prompt_format": tool_prompt_format,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                inference_chat_completion_params.InferenceChatCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionResponse,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionResponseStreamChunk],
        )


class AsyncInferenceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-api-python#with_streaming_response
        """
        return AsyncInferenceResourceWithStreamingResponse(self)

    @overload
    async def chat_completion(
        self,
        *,
        messages: Iterable[MessageParam],
        model_id: str,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: inference_chat_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation

          model_id: The identifier of the model to use.

          logprobs: If specified, log probabilities for each token position will be returned.

          response_format: Grammar specification for guided (structured) decoding. There are two options: -
              `ResponseFormat.json_schema`: The grammar is a JSON schema. Most providers
              support this format. - `ResponseFormat.grammar`: The grammar is a BNF grammar.
              This format is more flexible, but not all providers support it.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          tool_choice: Whether tool use is required or automatic. Defaults to ToolChoice.auto. ..
              deprecated:: Use tool_config instead.

          tool_config: Configuration for tool use.

          tool_prompt_format: Instructs the model how to format tool calls. By default, Llama Stack will
              attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: List of tool definitions available to the model

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def chat_completion(
        self,
        *,
        messages: Iterable[MessageParam],
        model_id: str,
        stream: Literal[True],
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: inference_chat_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation

          model_id: The identifier of the model to use.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          logprobs: If specified, log probabilities for each token position will be returned.

          response_format: Grammar specification for guided (structured) decoding. There are two options: -
              `ResponseFormat.json_schema`: The grammar is a JSON schema. Most providers
              support this format. - `ResponseFormat.grammar`: The grammar is a BNF grammar.
              This format is more flexible, but not all providers support it.

          tool_choice: Whether tool use is required or automatic. Defaults to ToolChoice.auto. ..
              deprecated:: Use tool_config instead.

          tool_config: Configuration for tool use.

          tool_prompt_format: Instructs the model how to format tool calls. By default, Llama Stack will
              attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: List of tool definitions available to the model

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def chat_completion(
        self,
        *,
        messages: Iterable[MessageParam],
        model_id: str,
        stream: bool,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: inference_chat_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse | AsyncStream[ChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation

          model_id: The identifier of the model to use.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          logprobs: If specified, log probabilities for each token position will be returned.

          response_format: Grammar specification for guided (structured) decoding. There are two options: -
              `ResponseFormat.json_schema`: The grammar is a JSON schema. Most providers
              support this format. - `ResponseFormat.grammar`: The grammar is a BNF grammar.
              This format is more flexible, but not all providers support it.

          tool_choice: Whether tool use is required or automatic. Defaults to ToolChoice.auto. ..
              deprecated:: Use tool_config instead.

          tool_config: Configuration for tool use.

          tool_prompt_format: Instructs the model how to format tool calls. By default, Llama Stack will
              attempt to use a format that is best adapted to the model. -
              `ToolPromptFormat.json`: The tool calls are formatted as a JSON object. -
              `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
              <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
              are output as Python syntax -- a list of function calls. .. deprecated:: Use
              tool_config instead.

          tools: List of tool definitions available to the model

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model_id"], ["messages", "model_id", "stream"])
    async def chat_completion(
        self,
        *,
        messages: Iterable[MessageParam],
        model_id: str,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: inference_chat_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_config: inference_chat_completion_params.ToolConfig | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionResponse | AsyncStream[ChatCompletionResponseStreamChunk]:
        return await self._post(
            "/v1/inference/chat-completion",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model_id": model_id,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "repetition_penalty": repetition_penalty,
                    "response_format": response_format,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tool_config": tool_config,
                    "tool_prompt_format": tool_prompt_format,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                inference_chat_completion_params.InferenceChatCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionResponse,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionResponseStreamChunk],
        )


class InferenceResourceWithRawResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.chat_completion = to_raw_response_wrapper(
            inference.chat_completion,
        )


class AsyncInferenceResourceWithRawResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.chat_completion = async_to_raw_response_wrapper(
            inference.chat_completion,
        )


class InferenceResourceWithStreamingResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.chat_completion = to_streamed_response_wrapper(
            inference.chat_completion,
        )


class AsyncInferenceResourceWithStreamingResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.chat_completion = async_to_streamed_response_wrapper(
            inference.chat_completion,
        )
