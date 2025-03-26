# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..text_content_item_param import TextContentItemParam
from ..image_content_item_param import ImageContentItemParam
from ..reasoning_content_item_param import ReasoningContentItemParam

__all__ = ["ToolResponseMessage", "ContentUnionMember1"]

ContentUnionMember1: TypeAlias = Union[ImageContentItemParam, TextContentItemParam, ReasoningContentItemParam]


class ToolResponseMessage(TypedDict, total=False):
    call_id: Required[str]
    """Unique identifier for the tool call this response is for"""

    content: Required[Union[str, Iterable[ContentUnionMember1]]]
    """The response content from the tool"""

    role: Required[Literal["tool"]]
    """Must be "tool" to identify this as a tool response"""
