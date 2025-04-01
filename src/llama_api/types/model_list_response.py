# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .ai_model import AIModel

__all__ = ["ModelListResponse"]


class ModelListResponse(BaseModel):
    data: List[AIModel]

    object: Optional[Literal["list"]] = None
