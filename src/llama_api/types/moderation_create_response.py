# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ModerationCreateResponse", "ModerationCreateResponseItem"]


class ModerationCreateResponseItem(BaseModel):
    flagged: bool

    flagged_categories: List[str]

    model: str


ModerationCreateResponse: TypeAlias = List[ModerationCreateResponseItem]
