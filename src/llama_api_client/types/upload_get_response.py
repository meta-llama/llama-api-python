# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UploadGetResponse"]


class UploadGetResponse(BaseModel):
    upload_id: str
    """The unique upload session identifier to use for uploading the file"""

    offset: Optional[int] = None
    """
    This is a zero-based numeric index of byte number in which the current upload
    session to be resuming upload from
    """
