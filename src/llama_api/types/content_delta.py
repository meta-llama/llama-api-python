# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ContentDelta",
    "TextDelta",
    "ImageDelta",
    "ToolCallDelta",
    "ToolCallDeltaToolCall",
    "ToolCallDeltaToolCallToolCall",
    "ReasoningContentDelta",
]


class TextDelta(BaseModel):
    text: str

    type: Literal["text"]


class ImageDelta(BaseModel):
    image: str

    type: Literal["image"]


class ToolCallDeltaToolCallToolCall(BaseModel):
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


ToolCallDeltaToolCall: TypeAlias = Union[str, ToolCallDeltaToolCallToolCall]


class ToolCallDelta(BaseModel):
    parse_status: Literal["started", "in_progress", "failed", "succeeded"]

    tool_call: ToolCallDeltaToolCall

    type: Literal["tool_call"]


class ReasoningContentDelta(BaseModel):
    answer: str

    reasoning: str

    type: Literal["reasoning"]


ContentDelta: TypeAlias = Annotated[
    Union[TextDelta, ImageDelta, ToolCallDelta, ReasoningContentDelta], PropertyInfo(discriminator="type")
]
