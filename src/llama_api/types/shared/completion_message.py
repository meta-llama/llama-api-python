# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "CompletionMessage",
    "Content",
    "ContentImageContentItem",
    "ContentImageContentItemImage",
    "ContentImageContentItemImageURL",
    "ContentTextContentItem",
    "ContentReasoningContentItem",
    "ToolCall",
]


class ContentImageContentItemImageURL(BaseModel):
    uri: str


class ContentImageContentItemImage(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[ContentImageContentItemImageURL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ContentImageContentItem(BaseModel):
    image: ContentImageContentItemImage
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """


class ContentTextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """


class ContentReasoningContentItem(BaseModel):
    answer: str
    """The final model response"""

    reasoning: str
    """The CoT reasoning content of the model"""

    type: Literal["reasoning"]
    """Discriminator type of the content item. Always "reasoning" """


Content: TypeAlias = Union[str, ContentImageContentItem, ContentTextContentItem, ContentReasoningContentItem]


class ToolCall(BaseModel):
    arguments: Union[
        str,
        Dict[
            str,
            Union[
                str, float, bool, List[Union[str, float, bool, None]], Dict[str, Union[str, float, bool, None]], None
            ],
        ],
    ]

    call_id: str

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]

    arguments_json: Optional[str] = None


class CompletionMessage(BaseModel):
    content: Content
    """The content of the model's response"""

    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    stop_reason: Literal["end_of_turn", "end_of_message", "out_of_tokens"]
    """Reason why the model stopped generating.

    Options are: - `StopReason.end_of_turn`: The model finished generating the
    entire response. - `StopReason.end_of_message`: The model finished generating
    but generated a partial response -- usually, a tool call. The user may call the
    tool and continue the conversation with the tool's response. -
    `StopReason.out_of_tokens`: The model ran out of token budget.
    """

    tool_calls: Optional[List[ToolCall]] = None
    """List of tool calls. Each tool call is a ToolCall object."""
