# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ChatCompletionResponse",
    "CompletionMessage",
    "CompletionMessageContentUnionMember1",
    "CompletionMessageContentUnionMember1ImageContentItem",
    "CompletionMessageContentUnionMember1ImageContentItemImage",
    "CompletionMessageContentUnionMember1ImageContentItemImageURL",
    "CompletionMessageContentUnionMember1TextContentItem",
    "CompletionMessageContentUnionMember1ReasoningContentItem",
    "CompletionMessageToolCall",
    "Logprob",
    "Metric",
]


class CompletionMessageContentUnionMember1ImageContentItemImageURL(BaseModel):
    uri: str


class CompletionMessageContentUnionMember1ImageContentItemImage(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[CompletionMessageContentUnionMember1ImageContentItemImageURL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class CompletionMessageContentUnionMember1ImageContentItem(BaseModel):
    image: CompletionMessageContentUnionMember1ImageContentItemImage
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """


class CompletionMessageContentUnionMember1TextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """


class CompletionMessageContentUnionMember1ReasoningContentItem(BaseModel):
    answer: str
    """The final model response"""

    reasoning: str
    """The CoT reasoning content of the model"""

    type: Literal["reasoning"]
    """Discriminator type of the content item. Always "reasoning" """


CompletionMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        CompletionMessageContentUnionMember1ImageContentItem,
        CompletionMessageContentUnionMember1TextContentItem,
        CompletionMessageContentUnionMember1ReasoningContentItem,
    ],
    PropertyInfo(discriminator="type"),
]


class CompletionMessageToolCall(BaseModel):
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
    content: Union[str, List[CompletionMessageContentUnionMember1]]
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

    tool_calls: Optional[List[CompletionMessageToolCall]] = None
    """List of tool calls. Each tool call is a ToolCall object."""


class Logprob(BaseModel):
    logprobs_by_token: Dict[str, float]
    """Dictionary mapping tokens to their log probabilities"""


class Metric(BaseModel):
    metric: str

    value: float

    unit: Optional[str] = None


class ChatCompletionResponse(BaseModel):
    completion_message: CompletionMessage
    """The complete response message"""

    logprobs: Optional[List[Logprob]] = None
    """Optional log probabilities for generated tokens"""

    metrics: Optional[List[Metric]] = None
