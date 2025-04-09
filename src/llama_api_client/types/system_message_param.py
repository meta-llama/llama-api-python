# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .message_text_content_item_param import MessageTextContentItemParam

__all__ = ["SystemMessageParam"]


class SystemMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageTextContentItemParam]]]
    """The content of the system message."""

    role: Required[Literal["system"]]
    """Must be "system" to identify this as a system message"""
