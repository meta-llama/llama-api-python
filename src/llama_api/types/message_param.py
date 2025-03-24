# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "MessageParam",
    "UserMessage",
    "UserMessageContentUnionMember1",
    "UserMessageContentUnionMember1ImageContentItem",
    "UserMessageContentUnionMember1ImageContentItemImage",
    "UserMessageContentUnionMember1ImageContentItemImageURL",
    "UserMessageContentUnionMember1TextContentItem",
    "UserMessageContentUnionMember1ReasoningContentItem",
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
    "CompletionMessage",
    "CompletionMessageContentUnionMember1",
    "CompletionMessageContentUnionMember1ImageContentItem",
    "CompletionMessageContentUnionMember1ImageContentItemImage",
    "CompletionMessageContentUnionMember1ImageContentItemImageURL",
    "CompletionMessageContentUnionMember1TextContentItem",
    "CompletionMessageContentUnionMember1ReasoningContentItem",
    "CompletionMessageToolCall",
]


class UserMessageContentUnionMember1ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class UserMessageContentUnionMember1ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: UserMessageContentUnionMember1ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class UserMessageContentUnionMember1ImageContentItem(TypedDict, total=False):
    image: Required[UserMessageContentUnionMember1ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class UserMessageContentUnionMember1TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class UserMessageContentUnionMember1ReasoningContentItem(TypedDict, total=False):
    answer: Required[str]
    """The final model response"""

    reasoning: Required[str]
    """The CoT reasoning content of the model"""

    type: Required[Literal["reasoning"]]
    """Discriminator type of the content item. Always "reasoning" """


UserMessageContentUnionMember1: TypeAlias = Union[
    UserMessageContentUnionMember1ImageContentItem,
    UserMessageContentUnionMember1TextContentItem,
    UserMessageContentUnionMember1ReasoningContentItem,
]


class UserMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[UserMessageContentUnionMember1]]]
    """The content of the message, which can include text and other media"""

    role: Required[Literal["user"]]
    """Must be "user" to identify this as a user message"""


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


class CompletionMessageContentUnionMember1ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class CompletionMessageContentUnionMember1ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: CompletionMessageContentUnionMember1ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class CompletionMessageContentUnionMember1ImageContentItem(TypedDict, total=False):
    image: Required[CompletionMessageContentUnionMember1ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class CompletionMessageContentUnionMember1TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class CompletionMessageContentUnionMember1ReasoningContentItem(TypedDict, total=False):
    answer: Required[str]
    """The final model response"""

    reasoning: Required[str]
    """The CoT reasoning content of the model"""

    type: Required[Literal["reasoning"]]
    """Discriminator type of the content item. Always "reasoning" """


CompletionMessageContentUnionMember1: TypeAlias = Union[
    CompletionMessageContentUnionMember1ImageContentItem,
    CompletionMessageContentUnionMember1TextContentItem,
    CompletionMessageContentUnionMember1ReasoningContentItem,
]


class CompletionMessageToolCall(TypedDict, total=False):
    arguments: Required[
        Union[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    List[Union[str, float, bool, None]],
                    Dict[str, Union[str, float, bool, None]],
                    None,
                ],
            ],
        ]
    ]

    call_id: Required[str]

    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

    arguments_json: str


class CompletionMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[CompletionMessageContentUnionMember1]]]
    """The content of the model's response"""

    role: Required[Literal["assistant"]]
    """Must be "assistant" to identify this as the model's response"""

    stop_reason: Required[Literal["end_of_turn", "end_of_message", "out_of_tokens"]]
    """Reason why the model stopped generating.

    Options are: - `StopReason.end_of_turn`: The model finished generating the
    entire response. - `StopReason.end_of_message`: The model finished generating
    but generated a partial response -- usually, a tool call. The user may call the
    tool and continue the conversation with the tool's response. -
    `StopReason.out_of_tokens`: The model ran out of token budget.
    """

    tool_calls: Iterable[CompletionMessageToolCall]
    """List of tool calls. Each tool call is a ToolCall object."""


MessageParam: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]
