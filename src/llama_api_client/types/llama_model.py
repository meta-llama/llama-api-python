# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LlamaModel"]


class LlamaModel(BaseModel):
    id: str
    """The unique model identifier, which can be referenced in the API."""

    created: int
    """The creation time of the model."""

    object: Literal["model"]
    """The object type, which is always "model" """

    owned_by: str
    """The owner of the model."""
