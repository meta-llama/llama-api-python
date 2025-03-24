# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "InterleavedContent",
    "UnionMember1",
    "UnionMember1ImageContentItem",
    "UnionMember1ImageContentItemImage",
    "UnionMember1ImageContentItemImageURL",
    "UnionMember1TextContentItem",
    "UnionMember1ReasoningContentItem",
]


class UnionMember1ImageContentItemImageURL(BaseModel):
    uri: str


class UnionMember1ImageContentItemImage(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[UnionMember1ImageContentItemImageURL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class UnionMember1ImageContentItem(BaseModel):
    image: UnionMember1ImageContentItemImage
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """


class UnionMember1TextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """


class UnionMember1ReasoningContentItem(BaseModel):
    answer: str
    """The final model response"""

    reasoning: str
    """The CoT reasoning content of the model"""

    type: Literal["reasoning"]
    """Discriminator type of the content item. Always "reasoning" """


UnionMember1: TypeAlias = Annotated[
    Union[UnionMember1ImageContentItem, UnionMember1TextContentItem, UnionMember1ReasoningContentItem],
    PropertyInfo(discriminator="type"),
]

InterleavedContent: TypeAlias = Union[str, List[UnionMember1]]
