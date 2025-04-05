# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..message_text_content_item import MessageTextContentItem
from ..message_image_content_item import MessageImageContentItem

__all__ = ["UserMessage", "ContentArrayOfContentItem"]

ContentArrayOfContentItem: TypeAlias = Annotated[
    Union[MessageTextContentItem, MessageImageContentItem], PropertyInfo(discriminator="type")
]


class UserMessage(BaseModel):
    content: Union[str, List[ContentArrayOfContentItem]]
    """The content of the user message, which can include text and other media."""

    role: Literal["user"]
    """Must be "user" to identify this as a user message."""
