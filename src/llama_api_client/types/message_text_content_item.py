# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageTextContentItem"]


class MessageTextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """
