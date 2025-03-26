# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .content_delta import ContentDelta

__all__ = ["ChatCompletionResponseEvent", "Logprob"]


class Logprob(BaseModel):
    logprobs_by_token: Dict[str, float]
    """Dictionary mapping tokens to their log probabilities"""


class ChatCompletionResponseEvent(BaseModel):
    delta: ContentDelta
    """Content generated since last event.

    This can be one or more tokens, or a tool call.
    """

    event_type: Literal["start", "complete", "progress"]
    """Type of the event"""

    logprobs: Optional[List[Logprob]] = None
    """Optional log probabilities for generated tokens"""

    stop_reason: Optional[Literal["end_of_turn", "end_of_message", "out_of_tokens"]] = None
    """Optional reason why generation stopped, if complete"""
