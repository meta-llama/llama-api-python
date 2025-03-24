# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .text_content_item import TextContentItem
from .image_content_item import ImageContentItem
from .reasoning_content_item import ReasoningContentItem

__all__ = ["InterleavedContentItem"]

InterleavedContentItem: TypeAlias = Annotated[
    Union[ImageContentItem, TextContentItem, ReasoningContentItem], PropertyInfo(discriminator="type")
]
