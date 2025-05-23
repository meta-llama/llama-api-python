# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...types.chat import completion_create_params
from ..._base_client import make_request_options
from ...types.message_param import MessageParam
from ...types.create_chat_completion_response import CreateChatCompletionResponse
from ...types.create_chat_completion_response_stream_chunk import CreateChatCompletionResponseStreamChunk

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meta-llama/llama-api-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meta-llama/llama-api-python#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        messages: Iterable[MessageParam],
        model: str,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateChatCompletionResponse:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use.

          max_completion_tokens: The maximum number of tokens to generate.

          repetition_penalty: Controls the likelyhood and generating repetitive responses.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs
              which ensures the model will match your supplied JSON schema. If not specified,
              the default is {"type": "text"}, and model will return a free-form text
              response.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          temperature: Controls randomness of the response by setting a temperature. Higher value leads
              to more creative responses. Lower values will make the response more focused and
              deterministic.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: List of tool definitions available to the model

          top_k: Only sample from the top K options for each subsequent token.

          top_p: Controls diversity of the response by setting a probability threshold when
              choosing the next token.

          user: A unique identifier representing your application end-user for monitoring abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[MessageParam],
        model: str,
        stream: Literal[True],
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[CreateChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          max_completion_tokens: The maximum number of tokens to generate.

          repetition_penalty: Controls the likelyhood and generating repetitive responses.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs
              which ensures the model will match your supplied JSON schema. If not specified,
              the default is {"type": "text"}, and model will return a free-form text
              response.

          temperature: Controls randomness of the response by setting a temperature. Higher value leads
              to more creative responses. Lower values will make the response more focused and
              deterministic.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: List of tool definitions available to the model

          top_k: Only sample from the top K options for each subsequent token.

          top_p: Controls diversity of the response by setting a probability threshold when
              choosing the next token.

          user: A unique identifier representing your application end-user for monitoring abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[MessageParam],
        model: str,
        stream: bool,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateChatCompletionResponse | Stream[CreateChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          max_completion_tokens: The maximum number of tokens to generate.

          repetition_penalty: Controls the likelyhood and generating repetitive responses.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs
              which ensures the model will match your supplied JSON schema. If not specified,
              the default is {"type": "text"}, and model will return a free-form text
              response.

          temperature: Controls randomness of the response by setting a temperature. Higher value leads
              to more creative responses. Lower values will make the response more focused and
              deterministic.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: List of tool definitions available to the model

          top_k: Only sample from the top K options for each subsequent token.

          top_p: Controls diversity of the response by setting a probability threshold when
              choosing the next token.

          user: A unique identifier representing your application end-user for monitoring abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    def create(
        self,
        *,
        messages: Iterable[MessageParam],
        model: str,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateChatCompletionResponse | Stream[CreateChatCompletionResponseStreamChunk]:
        if stream:
            extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "max_completion_tokens": max_completion_tokens,
                    "repetition_penalty": repetition_penalty,
                    "response_format": response_format,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                    "user": user,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateChatCompletionResponse,
            stream=stream or False,
            stream_cls=Stream[CreateChatCompletionResponseStreamChunk],
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meta-llama/llama-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meta-llama/llama-api-python#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        messages: Iterable[MessageParam],
        model: str,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateChatCompletionResponse:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use.

          max_completion_tokens: The maximum number of tokens to generate.

          repetition_penalty: Controls the likelyhood and generating repetitive responses.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs
              which ensures the model will match your supplied JSON schema. If not specified,
              the default is {"type": "text"}, and model will return a free-form text
              response.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          temperature: Controls randomness of the response by setting a temperature. Higher value leads
              to more creative responses. Lower values will make the response more focused and
              deterministic.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: List of tool definitions available to the model

          top_k: Only sample from the top K options for each subsequent token.

          top_p: Controls diversity of the response by setting a probability threshold when
              choosing the next token.

          user: A unique identifier representing your application end-user for monitoring abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[MessageParam],
        model: str,
        stream: Literal[True],
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[CreateChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          max_completion_tokens: The maximum number of tokens to generate.

          repetition_penalty: Controls the likelyhood and generating repetitive responses.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs
              which ensures the model will match your supplied JSON schema. If not specified,
              the default is {"type": "text"}, and model will return a free-form text
              response.

          temperature: Controls randomness of the response by setting a temperature. Higher value leads
              to more creative responses. Lower values will make the response more focused and
              deterministic.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: List of tool definitions available to the model

          top_k: Only sample from the top K options for each subsequent token.

          top_p: Controls diversity of the response by setting a probability threshold when
              choosing the next token.

          user: A unique identifier representing your application end-user for monitoring abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[MessageParam],
        model: str,
        stream: bool,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateChatCompletionResponse | AsyncStream[CreateChatCompletionResponseStreamChunk]:
        """
        Generate a chat completion for the given messages using the specified model.

        Args:
          messages: List of messages in the conversation.

          model: The identifier of the model to use.

          stream: If True, generate an SSE event stream of the response. Defaults to False.

          max_completion_tokens: The maximum number of tokens to generate.

          repetition_penalty: Controls the likelyhood and generating repetitive responses.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs
              which ensures the model will match your supplied JSON schema. If not specified,
              the default is {"type": "text"}, and model will return a free-form text
              response.

          temperature: Controls randomness of the response by setting a temperature. Higher value leads
              to more creative responses. Lower values will make the response more focused and
              deterministic.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: List of tool definitions available to the model

          top_k: Only sample from the top K options for each subsequent token.

          top_p: Controls diversity of the response by setting a probability threshold when
              choosing the next token.

          user: A unique identifier representing your application end-user for monitoring abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    async def create(
        self,
        *,
        messages: Iterable[MessageParam],
        model: str,
        max_completion_tokens: int | NotGiven = NOT_GIVEN,
        repetition_penalty: float | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateChatCompletionResponse | AsyncStream[CreateChatCompletionResponseStreamChunk]:
        if stream:
            extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "max_completion_tokens": max_completion_tokens,
                    "repetition_penalty": repetition_penalty,
                    "response_format": response_format,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                    "user": user,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateChatCompletionResponse,
            stream=stream or False,
            stream_cls=AsyncStream[CreateChatCompletionResponseStreamChunk],
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
