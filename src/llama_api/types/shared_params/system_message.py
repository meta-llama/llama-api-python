# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SystemMessage",
    "ContentUnionMember1",
    "ContentUnionMember1ImageContentItem",
    "ContentUnionMember1ImageContentItemImage",
    "ContentUnionMember1ImageContentItemImageURL",
    "ContentUnionMember1TextContentItem",
    "ContentUnionMember1ReasoningContentItem",
]


class ContentUnionMember1ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class ContentUnionMember1ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: ContentUnionMember1ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ContentUnionMember1ImageContentItem(TypedDict, total=False):
    image: Required[ContentUnionMember1ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class ContentUnionMember1TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class ContentUnionMember1ReasoningContentItem(TypedDict, total=False):
    answer: Required[str]
    """The final model response"""

    reasoning: Required[str]
    """The CoT reasoning content of the model"""

    type: Required[Literal["reasoning"]]
    """Discriminator type of the content item. Always "reasoning" """


ContentUnionMember1: TypeAlias = Union[
    ContentUnionMember1ImageContentItem, ContentUnionMember1TextContentItem, ContentUnionMember1ReasoningContentItem
]


class SystemMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[ContentUnionMember1]]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated.
    """

    role: Required[Literal["system"]]
    """Must be "system" to identify this as a system message"""
