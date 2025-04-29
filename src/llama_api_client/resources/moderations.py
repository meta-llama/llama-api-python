# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import moderation_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.message_param import MessageParam
from ..types.moderation_create_response import ModerationCreateResponse

__all__ = ["ModerationsResource", "AsyncModerationsResource"]


class ModerationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meta-llama/llama-api-python#accessing-raw-response-data-eg-headers
        """
        return ModerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meta-llama/llama-api-python#with_streaming_response
        """
        return ModerationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messages: Iterable[MessageParam],
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModerationCreateResponse:
        """
        Classifies if given messages are potentially harmful across several categories.

        Args:
          messages: List of messages in the conversation.

          model: Optional identifier of the model to use. Defaults to "Llama-Guard".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/moderations",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                },
                moderation_create_params.ModerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerationCreateResponse,
        )


class AsyncModerationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meta-llama/llama-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meta-llama/llama-api-python#with_streaming_response
        """
        return AsyncModerationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messages: Iterable[MessageParam],
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModerationCreateResponse:
        """
        Classifies if given messages are potentially harmful across several categories.

        Args:
          messages: List of messages in the conversation.

          model: Optional identifier of the model to use. Defaults to "Llama-Guard".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/moderations",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                },
                moderation_create_params.ModerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerationCreateResponse,
        )


class ModerationsResourceWithRawResponse:
    def __init__(self, moderations: ModerationsResource) -> None:
        self._moderations = moderations

        self.create = to_raw_response_wrapper(
            moderations.create,
        )


class AsyncModerationsResourceWithRawResponse:
    def __init__(self, moderations: AsyncModerationsResource) -> None:
        self._moderations = moderations

        self.create = async_to_raw_response_wrapper(
            moderations.create,
        )


class ModerationsResourceWithStreamingResponse:
    def __init__(self, moderations: ModerationsResource) -> None:
        self._moderations = moderations

        self.create = to_streamed_response_wrapper(
            moderations.create,
        )


class AsyncModerationsResourceWithStreamingResponse:
    def __init__(self, moderations: AsyncModerationsResource) -> None:
        self._moderations = moderations

        self.create = async_to_streamed_response_wrapper(
            moderations.create,
        )
