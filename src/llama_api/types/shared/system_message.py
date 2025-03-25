# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel
from ..interleaved_content_item import InterleavedContentItem

__all__ = ["SystemMessage"]


class SystemMessage(BaseModel):
    content: Union[str, List[InterleavedContentItem]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated.
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""
