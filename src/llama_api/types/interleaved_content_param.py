# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "InterleavedContentParam",
    "UnionMember1",
    "UnionMember1ImageContentItem",
    "UnionMember1ImageContentItemImage",
    "UnionMember1ImageContentItemImageURL",
    "UnionMember1TextContentItem",
    "UnionMember1ReasoningContentItem",
]


class UnionMember1ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class UnionMember1ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: UnionMember1ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class UnionMember1ImageContentItem(TypedDict, total=False):
    image: Required[UnionMember1ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class UnionMember1TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class UnionMember1ReasoningContentItem(TypedDict, total=False):
    answer: Required[str]
    """The final model response"""

    reasoning: Required[str]
    """The CoT reasoning content of the model"""

    type: Required[Literal["reasoning"]]
    """Discriminator type of the content item. Always "reasoning" """


UnionMember1: TypeAlias = Union[
    UnionMember1ImageContentItem, UnionMember1TextContentItem, UnionMember1ReasoningContentItem
]

InterleavedContentParam: TypeAlias = Union[str, Iterable[UnionMember1]]
