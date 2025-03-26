# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel
from ..interleaved_content_item import InterleavedContentItem

__all__ = ["UserMessage"]


class UserMessage(BaseModel):
    content: Union[str, List[InterleavedContentItem]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""
