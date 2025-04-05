# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel
from ..message_text_content_item import MessageTextContentItem

__all__ = ["SystemMessage"]


class SystemMessage(BaseModel):
    content: Union[str, List[MessageTextContentItem]]
    """The content of the system message."""

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""
