# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UploadCreateParams"]


class UploadCreateParams(TypedDict, total=False):
    bytes: Required[int]
    """The number of bytes in the file you are uploading"""

    filename: Required[str]
    """The name of the file to upload"""

    mime_type: Required[
        Literal[
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
        ]
    ]
    """The MIME type of the file.

    Must be one of the supported MIME type for the given purpose.
    """

    purpose: Required[
        Literal[
            "attachment",
            "ephemeral_attachment",
            "image_generation_result",
            "messages_finetune",
            "messages_eval",
            "metadata",
        ]
    ]
    """Intended purpose of the uploaded file."""

    x_api_version: Annotated[Literal["1.0.0"], PropertyInfo(alias="X-API-Version")]
