# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..text_content_item_param import TextContentItemParam
from ..image_content_item_param import ImageContentItemParam
from ..reasoning_content_item_param import ReasoningContentItemParam

__all__ = ["UserMessage", "ContentUnionMember1"]

ContentUnionMember1: TypeAlias = Union[ImageContentItemParam, TextContentItemParam, ReasoningContentItemParam]


class UserMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[ContentUnionMember1]]]
    """The content of the message, which can include text and other media"""

    role: Required[Literal["user"]]
    """Must be "user" to identify this as a user message"""
