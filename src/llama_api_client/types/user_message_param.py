# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .message_text_content_item_param import MessageTextContentItemParam
from .message_image_content_item_param import MessageImageContentItemParam

__all__ = ["UserMessageParam", "ContentArrayOfContentItem"]

ContentArrayOfContentItem: TypeAlias = Union[MessageTextContentItemParam, MessageImageContentItemParam]


class UserMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[ContentArrayOfContentItem]]]
    """The content of the user message, which can include text and other media."""

    role: Required[Literal["user"]]
    """Must be "user" to identify this as a user message."""
