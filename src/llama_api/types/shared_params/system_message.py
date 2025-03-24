# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..interleaved_content_param import InterleavedContentParam

__all__ = ["SystemMessage"]


class SystemMessage(TypedDict, total=False):
    content: Required[InterleavedContentParam]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated.
    """

    role: Required[Literal["system"]]
    """Must be "system" to identify this as a system message"""
