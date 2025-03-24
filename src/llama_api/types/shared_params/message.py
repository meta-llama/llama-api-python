# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .user_message import UserMessage
from .completion_message import CompletionMessage

__all__ = [
    "Message",
    "SystemMessage",
    "SystemMessageContentUnionMember1",
    "SystemMessageContentUnionMember1ImageContentItem",
    "SystemMessageContentUnionMember1ImageContentItemImage",
    "SystemMessageContentUnionMember1ImageContentItemImageURL",
    "SystemMessageContentUnionMember1TextContentItem",
    "SystemMessageContentUnionMember1ReasoningContentItem",
    "ToolResponseMessage",
    "ToolResponseMessageContentUnionMember1",
    "ToolResponseMessageContentUnionMember1ImageContentItem",
    "ToolResponseMessageContentUnionMember1ImageContentItemImage",
    "ToolResponseMessageContentUnionMember1ImageContentItemImageURL",
    "ToolResponseMessageContentUnionMember1TextContentItem",
    "ToolResponseMessageContentUnionMember1ReasoningContentItem",
]


class SystemMessageContentUnionMember1ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class SystemMessageContentUnionMember1ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: SystemMessageContentUnionMember1ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class SystemMessageContentUnionMember1ImageContentItem(TypedDict, total=False):
    image: Required[SystemMessageContentUnionMember1ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class SystemMessageContentUnionMember1TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class SystemMessageContentUnionMember1ReasoningContentItem(TypedDict, total=False):
    answer: Required[str]
    """The final model response"""

    reasoning: Required[str]
    """The CoT reasoning content of the model"""

    type: Required[Literal["reasoning"]]
    """Discriminator type of the content item. Always "reasoning" """


SystemMessageContentUnionMember1: TypeAlias = Union[
    SystemMessageContentUnionMember1ImageContentItem,
    SystemMessageContentUnionMember1TextContentItem,
    SystemMessageContentUnionMember1ReasoningContentItem,
]


class SystemMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[SystemMessageContentUnionMember1]]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated.
    """

    role: Required[Literal["system"]]
    """Must be "system" to identify this as a system message"""


class ToolResponseMessageContentUnionMember1ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class ToolResponseMessageContentUnionMember1ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: ToolResponseMessageContentUnionMember1ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ToolResponseMessageContentUnionMember1ImageContentItem(TypedDict, total=False):
    image: Required[ToolResponseMessageContentUnionMember1ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class ToolResponseMessageContentUnionMember1TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class ToolResponseMessageContentUnionMember1ReasoningContentItem(TypedDict, total=False):
    answer: Required[str]
    """The final model response"""

    reasoning: Required[str]
    """The CoT reasoning content of the model"""

    type: Required[Literal["reasoning"]]
    """Discriminator type of the content item. Always "reasoning" """


ToolResponseMessageContentUnionMember1: TypeAlias = Union[
    ToolResponseMessageContentUnionMember1ImageContentItem,
    ToolResponseMessageContentUnionMember1TextContentItem,
    ToolResponseMessageContentUnionMember1ReasoningContentItem,
]


class ToolResponseMessage(TypedDict, total=False):
    call_id: Required[str]
    """Unique identifier for the tool call this response is for"""

    content: Required[Union[str, Iterable[ToolResponseMessageContentUnionMember1]]]
    """The response content from the tool"""

    role: Required[Literal["tool"]]
    """Must be "tool" to identify this as a tool response"""


Message: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]
