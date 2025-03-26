# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..text_content_item_param import TextContentItemParam
from ..image_content_item_param import ImageContentItemParam
from ..reasoning_content_item_param import ReasoningContentItemParam

__all__ = ["SystemMessage", "ContentUnionMember1"]

ContentUnionMember1: TypeAlias = Union[ImageContentItemParam, TextContentItemParam, ReasoningContentItemParam]


class SystemMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[ContentUnionMember1]]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated.
    """

    role: Required[Literal["system"]]
    """Must be "system" to identify this as a system message"""
