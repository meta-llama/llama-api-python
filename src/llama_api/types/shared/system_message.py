# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..text_content_item import TextContentItem
from ..image_content_item import ImageContentItem
from ..reasoning_content_item import ReasoningContentItem

__all__ = ["SystemMessage", "ContentUnionMember1"]

ContentUnionMember1: TypeAlias = Annotated[
    Union[ImageContentItem, TextContentItem, ReasoningContentItem], PropertyInfo(discriminator="type")
]


class SystemMessage(BaseModel):
    content: Union[str, List[ContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated.
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""
