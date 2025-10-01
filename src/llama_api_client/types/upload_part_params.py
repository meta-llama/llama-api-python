# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["UploadPartParams"]


class UploadPartParams(TypedDict, total=False):
    data: Required[FileTypes]
    """The chunk of bytes to upload"""

    x_api_version: Annotated[Literal["1.0.0"], PropertyInfo(alias="X-API-Version")]

    x_upload_offset: Annotated[int, PropertyInfo(alias="X-Upload-Offset")]
