# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageTextContentItemParam"]


class MessageTextContentItemParam(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """
