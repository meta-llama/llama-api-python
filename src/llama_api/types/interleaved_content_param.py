# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias

from .interleaved_content_item_param import InterleavedContentItemParam

__all__ = ["InterleavedContentParam"]

InterleavedContentParam: TypeAlias = Union[str, Iterable[InterleavedContentItemParam]]
