# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import upload_part_params, upload_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import is_given, extract_files, maybe_transform, strip_not_given, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.upload_get_response import UploadGetResponse
from ..types.upload_part_response import UploadPartResponse
from ..types.upload_create_response import UploadCreateResponse

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meta-llama/llama-api-python#accessing-raw-response-data-eg-headers
        """
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meta-llama/llama-api-python#with_streaming_response
        """
        return UploadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bytes: int,
        filename: str,
        mime_type: Literal[
            "image/jpeg",
            "image/jpg",
            "image/png",
            "image/gif",
            "image/webp",
            "image/x-icon",
            "audio/mp3",
            "audio/mpeg",
            "audio/wav",
            "audio/x-wav",
            "application/jsonl",
            "application/json",
            "text/plain",
            "video/mp4",
            "application/pdf",
        ],
        purpose: Literal[
            "attachment",
            "ephemeral_attachment",
            "image_generation_result",
            "messages_finetune",
            "messages_eval",
            "metadata",
        ],
        x_api_version: Literal["1.0.0"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCreateResponse:
        """
        Initiate an upload session with specified file metadata

        Args:
          bytes: The number of bytes in the file you are uploading

          filename: The name of the file to upload

          mime_type: The MIME type of the file. Must be one of the supported MIME type for the given
              purpose.

          purpose: Intended purpose of the uploaded file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"X-API-Version": str(x_api_version) if is_given(x_api_version) else not_given}),
            **(extra_headers or {}),
        }
        return self._post(
            "/uploads",
            body=maybe_transform(
                {
                    "bytes": bytes,
                    "filename": filename,
                    "mime_type": mime_type,
                    "purpose": purpose,
                },
                upload_create_params.UploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCreateResponse,
        )

    def get(
        self,
        upload_id: str,
        *,
        x_api_version: Literal["1.0.0"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadGetResponse:
        """
        Get the status of the given upload session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        extra_headers = {
            **strip_not_given({"X-API-Version": str(x_api_version) if is_given(x_api_version) else not_given}),
            **(extra_headers or {}),
        }
        return self._get(
            f"/uploads/{upload_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadGetResponse,
        )

    def part(
        self,
        upload_id: str,
        *,
        data: FileTypes,
        x_api_version: Literal["1.0.0"] | Omit = omit,
        x_upload_offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadPartResponse:
        """
        Upload a chunk of bytes to the upload session

        Args:
          data: The chunk of bytes to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": str(x_api_version) if is_given(x_api_version) else not_given,
                    "X-Upload-Offset": str(x_upload_offset) if is_given(x_upload_offset) else not_given,
                }
            ),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal({"data": data})
        files = extract_files(cast(Mapping[str, object], body), paths=[["data"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/uploads/{upload_id}",
            body=maybe_transform(body, upload_part_params.UploadPartParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadPartResponse,
        )


class AsyncUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meta-llama/llama-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meta-llama/llama-api-python#with_streaming_response
        """
        return AsyncUploadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bytes: int,
        filename: str,
        mime_type: Literal[
            "image/jpeg",
            "image/jpg",
            "image/png",
            "image/gif",
            "image/webp",
            "image/x-icon",
            "audio/mp3",
            "audio/mpeg",
            "audio/wav",
            "audio/x-wav",
            "application/jsonl",
            "application/json",
            "text/plain",
            "video/mp4",
            "application/pdf",
        ],
        purpose: Literal[
            "attachment",
            "ephemeral_attachment",
            "image_generation_result",
            "messages_finetune",
            "messages_eval",
            "metadata",
        ],
        x_api_version: Literal["1.0.0"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCreateResponse:
        """
        Initiate an upload session with specified file metadata

        Args:
          bytes: The number of bytes in the file you are uploading

          filename: The name of the file to upload

          mime_type: The MIME type of the file. Must be one of the supported MIME type for the given
              purpose.

          purpose: Intended purpose of the uploaded file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"X-API-Version": str(x_api_version) if is_given(x_api_version) else not_given}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/uploads",
            body=await async_maybe_transform(
                {
                    "bytes": bytes,
                    "filename": filename,
                    "mime_type": mime_type,
                    "purpose": purpose,
                },
                upload_create_params.UploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCreateResponse,
        )

    async def get(
        self,
        upload_id: str,
        *,
        x_api_version: Literal["1.0.0"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadGetResponse:
        """
        Get the status of the given upload session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        extra_headers = {
            **strip_not_given({"X-API-Version": str(x_api_version) if is_given(x_api_version) else not_given}),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/uploads/{upload_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadGetResponse,
        )

    async def part(
        self,
        upload_id: str,
        *,
        data: FileTypes,
        x_api_version: Literal["1.0.0"] | Omit = omit,
        x_upload_offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadPartResponse:
        """
        Upload a chunk of bytes to the upload session

        Args:
          data: The chunk of bytes to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-API-Version": str(x_api_version) if is_given(x_api_version) else not_given,
                    "X-Upload-Offset": str(x_upload_offset) if is_given(x_upload_offset) else not_given,
                }
            ),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal({"data": data})
        files = extract_files(cast(Mapping[str, object], body), paths=[["data"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/uploads/{upload_id}",
            body=await async_maybe_transform(body, upload_part_params.UploadPartParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadPartResponse,
        )


class UploadsResourceWithRawResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_raw_response_wrapper(
            uploads.create,
        )
        self.get = to_raw_response_wrapper(
            uploads.get,
        )
        self.part = to_raw_response_wrapper(
            uploads.part,
        )


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_raw_response_wrapper(
            uploads.create,
        )
        self.get = async_to_raw_response_wrapper(
            uploads.get,
        )
        self.part = async_to_raw_response_wrapper(
            uploads.part,
        )


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_streamed_response_wrapper(
            uploads.create,
        )
        self.get = to_streamed_response_wrapper(
            uploads.get,
        )
        self.part = to_streamed_response_wrapper(
            uploads.part,
        )


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_streamed_response_wrapper(
            uploads.create,
        )
        self.get = async_to_streamed_response_wrapper(
            uploads.get,
        )
        self.part = async_to_streamed_response_wrapper(
            uploads.part,
        )
