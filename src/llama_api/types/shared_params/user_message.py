# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..interleaved_content_item_param import InterleavedContentItemParam

__all__ = ["UserMessage"]


class UserMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[InterleavedContentItemParam]]]
    """The content of the message, which can include text and other media"""

    role: Required[Literal["user"]]
    """Must be "user" to identify this as a user message"""
