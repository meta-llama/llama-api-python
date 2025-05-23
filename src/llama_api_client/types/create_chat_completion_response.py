# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .completion_message import CompletionMessage

__all__ = ["CreateChatCompletionResponse", "Metric"]


class Metric(BaseModel):
    metric: str

    value: float

    unit: Optional[str] = None


class CreateChatCompletionResponse(BaseModel):
    completion_message: CompletionMessage
    """The complete response message"""

    id: Optional[str] = None
    """The unique identifier of the chat completion request."""

    metrics: Optional[List[Metric]] = None
