# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..text_content_item import TextContentItem
from ..image_content_item import ImageContentItem
from ..reasoning_content_item import ReasoningContentItem

__all__ = ["ToolResponseMessage", "ContentUnionMember1"]

ContentUnionMember1: TypeAlias = Annotated[
    Union[ImageContentItem, TextContentItem, ReasoningContentItem], PropertyInfo(discriminator="type")
]


class ToolResponseMessage(BaseModel):
    call_id: str
    """Unique identifier for the tool call this response is for"""

    content: Union[str, List[ContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""
