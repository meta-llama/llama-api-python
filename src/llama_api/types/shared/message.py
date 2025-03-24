# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
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


class SystemMessageContentUnionMember1ImageContentItemImageURL(BaseModel):
    uri: str


class SystemMessageContentUnionMember1ImageContentItemImage(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[SystemMessageContentUnionMember1ImageContentItemImageURL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class SystemMessageContentUnionMember1ImageContentItem(BaseModel):
    image: SystemMessageContentUnionMember1ImageContentItemImage
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """


class SystemMessageContentUnionMember1TextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """


class SystemMessageContentUnionMember1ReasoningContentItem(BaseModel):
    answer: str
    """The final model response"""

    reasoning: str
    """The CoT reasoning content of the model"""

    type: Literal["reasoning"]
    """Discriminator type of the content item. Always "reasoning" """


SystemMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        SystemMessageContentUnionMember1ImageContentItem,
        SystemMessageContentUnionMember1TextContentItem,
        SystemMessageContentUnionMember1ReasoningContentItem,
    ],
    PropertyInfo(discriminator="type"),
]


class SystemMessage(BaseModel):
    content: Union[str, List[SystemMessageContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated.
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""


class ToolResponseMessageContentUnionMember1ImageContentItemImageURL(BaseModel):
    uri: str


class ToolResponseMessageContentUnionMember1ImageContentItemImage(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[ToolResponseMessageContentUnionMember1ImageContentItemImageURL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ToolResponseMessageContentUnionMember1ImageContentItem(BaseModel):
    image: ToolResponseMessageContentUnionMember1ImageContentItemImage
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """


class ToolResponseMessageContentUnionMember1TextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """


class ToolResponseMessageContentUnionMember1ReasoningContentItem(BaseModel):
    answer: str
    """The final model response"""

    reasoning: str
    """The CoT reasoning content of the model"""

    type: Literal["reasoning"]
    """Discriminator type of the content item. Always "reasoning" """


ToolResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        ToolResponseMessageContentUnionMember1ImageContentItem,
        ToolResponseMessageContentUnionMember1TextContentItem,
        ToolResponseMessageContentUnionMember1ReasoningContentItem,
    ],
    PropertyInfo(discriminator="type"),
]


class ToolResponseMessage(BaseModel):
    call_id: str
    """Unique identifier for the tool call this response is for"""

    content: Union[str, List[ToolResponseMessageContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""


Message: TypeAlias = Annotated[
    Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage], PropertyInfo(discriminator="role")
]
