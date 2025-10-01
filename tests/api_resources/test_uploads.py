# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_api_client import LlamaAPIClient, AsyncLlamaAPIClient
from llama_api_client.types import (
    UploadGetResponse,
    UploadPartResponse,
    UploadCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaAPIClient) -> None:
        upload = client.uploads.create(
            bytes=0,
            filename="filename",
            mime_type="image/jpeg",
            purpose="attachment",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaAPIClient) -> None:
        upload = client.uploads.create(
            bytes=0,
            filename="filename",
            mime_type="image/jpeg",
            purpose="attachment",
            x_api_version="1.0.0",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaAPIClient) -> None:
        response = client.uploads.with_raw_response.create(
            bytes=0,
            filename="filename",
            mime_type="image/jpeg",
            purpose="attachment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaAPIClient) -> None:
        with client.uploads.with_streaming_response.create(
            bytes=0,
            filename="filename",
            mime_type="image/jpeg",
            purpose="attachment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadCreateResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaAPIClient) -> None:
        upload = client.uploads.get(
            upload_id="upload_id",
        )
        assert_matches_type(UploadGetResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaAPIClient) -> None:
        upload = client.uploads.get(
            upload_id="upload_id",
            x_api_version="1.0.0",
        )
        assert_matches_type(UploadGetResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaAPIClient) -> None:
        response = client.uploads.with_raw_response.get(
            upload_id="upload_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadGetResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaAPIClient) -> None:
        with client.uploads.with_streaming_response.get(
            upload_id="upload_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadGetResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaAPIClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.uploads.with_raw_response.get(
                upload_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_part(self, client: LlamaAPIClient) -> None:
        upload = client.uploads.part(
            upload_id="upload_id",
            data=b"raw file contents",
        )
        assert_matches_type(UploadPartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_part_with_all_params(self, client: LlamaAPIClient) -> None:
        upload = client.uploads.part(
            upload_id="upload_id",
            data=b"raw file contents",
            x_api_version="1.0.0",
            x_upload_offset=0,
        )
        assert_matches_type(UploadPartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_part(self, client: LlamaAPIClient) -> None:
        response = client.uploads.with_raw_response.part(
            upload_id="upload_id",
            data=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadPartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_part(self, client: LlamaAPIClient) -> None:
        with client.uploads.with_streaming_response.part(
            upload_id="upload_id",
            data=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadPartResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_part(self, client: LlamaAPIClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.uploads.with_raw_response.part(
                upload_id="",
                data=b"raw file contents",
            )


class TestAsyncUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaAPIClient) -> None:
        upload = await async_client.uploads.create(
            bytes=0,
            filename="filename",
            mime_type="image/jpeg",
            purpose="attachment",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaAPIClient) -> None:
        upload = await async_client.uploads.create(
            bytes=0,
            filename="filename",
            mime_type="image/jpeg",
            purpose="attachment",
            x_api_version="1.0.0",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaAPIClient) -> None:
        response = await async_client.uploads.with_raw_response.create(
            bytes=0,
            filename="filename",
            mime_type="image/jpeg",
            purpose="attachment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaAPIClient) -> None:
        async with async_client.uploads.with_streaming_response.create(
            bytes=0,
            filename="filename",
            mime_type="image/jpeg",
            purpose="attachment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadCreateResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaAPIClient) -> None:
        upload = await async_client.uploads.get(
            upload_id="upload_id",
        )
        assert_matches_type(UploadGetResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaAPIClient) -> None:
        upload = await async_client.uploads.get(
            upload_id="upload_id",
            x_api_version="1.0.0",
        )
        assert_matches_type(UploadGetResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaAPIClient) -> None:
        response = await async_client.uploads.with_raw_response.get(
            upload_id="upload_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadGetResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaAPIClient) -> None:
        async with async_client.uploads.with_streaming_response.get(
            upload_id="upload_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadGetResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaAPIClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.uploads.with_raw_response.get(
                upload_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_part(self, async_client: AsyncLlamaAPIClient) -> None:
        upload = await async_client.uploads.part(
            upload_id="upload_id",
            data=b"raw file contents",
        )
        assert_matches_type(UploadPartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_part_with_all_params(self, async_client: AsyncLlamaAPIClient) -> None:
        upload = await async_client.uploads.part(
            upload_id="upload_id",
            data=b"raw file contents",
            x_api_version="1.0.0",
            x_upload_offset=0,
        )
        assert_matches_type(UploadPartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_part(self, async_client: AsyncLlamaAPIClient) -> None:
        response = await async_client.uploads.with_raw_response.part(
            upload_id="upload_id",
            data=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadPartResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_part(self, async_client: AsyncLlamaAPIClient) -> None:
        async with async_client.uploads.with_streaming_response.part(
            upload_id="upload_id",
            data=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadPartResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_part(self, async_client: AsyncLlamaAPIClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.uploads.with_raw_response.part(
                upload_id="",
                data=b"raw file contents",
            )
