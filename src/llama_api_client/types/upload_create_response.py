# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UploadCreateResponse"]


class UploadCreateResponse(BaseModel):
    id: str
    """The unique upload session identifier to use for uploading the file"""

    bytes: int
    """The number of bytes in the file you are uploading"""

    filename: str
    """The name of the file to upload"""

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
    ]
    """The MIME type of the file.

    Must be one of the supported MIME type for the given purpose.
    """

    purpose: Literal[
        "attachment",
        "ephemeral_attachment",
        "image_generation_result",
        "messages_finetune",
        "messages_eval",
        "metadata",
    ]
    """Intended purpose of the uploaded file."""
