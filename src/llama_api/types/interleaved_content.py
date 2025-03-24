# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .interleaved_content_item import InterleavedContentItem

__all__ = ["InterleavedContent"]

InterleavedContent: TypeAlias = Union[str, List[InterleavedContentItem]]
