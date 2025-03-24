# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CompletionMessage",
    "ContentUnionMember1",
    "ContentUnionMember1ImageContentItem",
    "ContentUnionMember1ImageContentItemImage",
    "ContentUnionMember1ImageContentItemImageURL",
    "ContentUnionMember1TextContentItem",
    "ContentUnionMember1ReasoningContentItem",
    "ToolCall",
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


class ToolCall(TypedDict, total=False):
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
    content: Required[Union[str, Iterable[ContentUnionMember1]]]
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

    tool_calls: Iterable[ToolCall]
    """List of tool calls. Each tool call is a ToolCall object."""
