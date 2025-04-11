# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .message_param import MessageParam

__all__ = ["ModerationCreateParams"]


class ModerationCreateParams(TypedDict, total=False):
    messages: Required[Iterable[MessageParam]]
    """List of messages in the conversation."""

    model: str
    """Optional identifier of the model to use. Defaults to "Llama-Guard"."""
