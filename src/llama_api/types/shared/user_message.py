# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..text_content_item import TextContentItem
from ..image_content_item import ImageContentItem
from ..reasoning_content_item import ReasoningContentItem

__all__ = ["UserMessage", "ContentUnionMember1"]

ContentUnionMember1: TypeAlias = Annotated[
    Union[ImageContentItem, TextContentItem, ReasoningContentItem], PropertyInfo(discriminator="type")
]


class UserMessage(BaseModel):
    content: Union[str, List[ContentUnionMember1]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""
