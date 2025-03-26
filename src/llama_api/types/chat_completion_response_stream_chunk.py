# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .chat_completion_response_event import ChatCompletionResponseEvent

__all__ = ["ChatCompletionResponseStreamChunk", "Metric"]


class Metric(BaseModel):
    metric: str

    value: float

    unit: Optional[str] = None


class ChatCompletionResponseStreamChunk(BaseModel):
    event: ChatCompletionResponseEvent
    """The event containing the new content"""

    metrics: Optional[List[Metric]] = None
