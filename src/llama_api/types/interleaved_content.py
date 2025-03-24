# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .text_content_item import TextContentItem
from .image_content_item import ImageContentItem
from .reasoning_content_item import ReasoningContentItem
from .interleaved_content_item import InterleavedContentItem

__all__ = ["InterleavedContent"]

InterleavedContent: TypeAlias = Union[
    str, ImageContentItem, TextContentItem, ReasoningContentItem, List[InterleavedContentItem]
]
