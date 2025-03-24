# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ChatCompletionResponseStreamChunk",
    "Event",
    "EventDelta",
    "EventDeltaTextDelta",
    "EventDeltaImageDelta",
    "EventDeltaToolCallDelta",
    "EventDeltaToolCallDeltaToolCall",
    "EventDeltaToolCallDeltaToolCallToolCall",
    "EventDeltaReasoningContentDelta",
    "EventLogprob",
    "Metric",
]


class EventDeltaTextDelta(BaseModel):
    text: str

    type: Literal["text"]


class EventDeltaImageDelta(BaseModel):
    image: str

    type: Literal["image"]


class EventDeltaToolCallDeltaToolCallToolCall(BaseModel):
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


EventDeltaToolCallDeltaToolCall: TypeAlias = Union[str, EventDeltaToolCallDeltaToolCallToolCall]


class EventDeltaToolCallDelta(BaseModel):
    parse_status: Literal["started", "in_progress", "failed", "succeeded"]

    tool_call: EventDeltaToolCallDeltaToolCall

    type: Literal["tool_call"]


class EventDeltaReasoningContentDelta(BaseModel):
    answer: str

    reasoning: str

    type: Literal["reasoning"]


EventDelta: TypeAlias = Annotated[
    Union[EventDeltaTextDelta, EventDeltaImageDelta, EventDeltaToolCallDelta, EventDeltaReasoningContentDelta],
    PropertyInfo(discriminator="type"),
]


class EventLogprob(BaseModel):
    logprobs_by_token: Dict[str, float]
    """Dictionary mapping tokens to their log probabilities"""


class Event(BaseModel):
    delta: EventDelta
    """Content generated since last event.

    This can be one or more tokens, or a tool call.
    """

    event_type: Literal["start", "complete", "progress"]
    """Type of the event"""

    logprobs: Optional[List[EventLogprob]] = None
    """Optional log probabilities for generated tokens"""

    stop_reason: Optional[Literal["end_of_turn", "end_of_message", "out_of_tokens"]] = None
    """Optional reason why generation stopped, if complete"""


class Metric(BaseModel):
    metric: str

    value: float

    unit: Optional[str] = None


class ChatCompletionResponseStreamChunk(BaseModel):
    event: Event
    """The event containing the new content"""

    metrics: Optional[List[Metric]] = None
