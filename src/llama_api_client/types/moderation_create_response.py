# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ModerationCreateResponse", "Result"]


class Result(BaseModel):
    flagged: bool

    flagged_categories: List[str]


class ModerationCreateResponse(BaseModel):
    model: str

    results: List[Result]
