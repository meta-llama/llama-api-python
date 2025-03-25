# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "SystemMessage",
    "ContentUnionMember1",
    "ContentUnionMember1ImageContentItem",
    "ContentUnionMember1ImageContentItemImage",
    "ContentUnionMember1ImageContentItemImageURL",
    "ContentUnionMember1TextContentItem",
    "ContentUnionMember1ReasoningContentItem",
]


class ContentUnionMember1ImageContentItemImageURL(BaseModel):
    uri: str


class ContentUnionMember1ImageContentItemImage(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[ContentUnionMember1ImageContentItemImageURL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ContentUnionMember1ImageContentItem(BaseModel):
    image: ContentUnionMember1ImageContentItemImage
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """


class ContentUnionMember1TextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """


class ContentUnionMember1ReasoningContentItem(BaseModel):
    answer: str
    """The final model response"""

    reasoning: str
    """The CoT reasoning content of the model"""

    type: Literal["reasoning"]
    """Discriminator type of the content item. Always "reasoning" """


ContentUnionMember1: TypeAlias = Annotated[
    Union[
        ContentUnionMember1ImageContentItem, ContentUnionMember1TextContentItem, ContentUnionMember1ReasoningContentItem
    ],
    PropertyInfo(discriminator="type"),
]


class SystemMessage(BaseModel):
    content: Union[str, List[ContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated.
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""
