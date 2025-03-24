# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ImageContentItem", "Image", "ImageURL"]


class ImageURL(BaseModel):
    uri: str


class Image(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[ImageURL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ImageContentItem(BaseModel):
    image: Image
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """
