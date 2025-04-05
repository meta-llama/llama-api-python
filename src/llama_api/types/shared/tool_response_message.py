# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel
from ..message_text_content_item import MessageTextContentItem

__all__ = ["ToolResponseMessage"]


class ToolResponseMessage(BaseModel):
    content: Union[str, List[MessageTextContentItem]]
    """The content of the user message, which can include text and other media."""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""
