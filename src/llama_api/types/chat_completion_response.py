# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .shared.completion_message import CompletionMessage

__all__ = ["ChatCompletionResponse", "Logprob", "Metric"]


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
