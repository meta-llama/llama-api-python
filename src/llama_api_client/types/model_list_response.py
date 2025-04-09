# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .llama_model import LlamaModel

__all__ = ["ModelListResponse"]

ModelListResponse: TypeAlias = List[LlamaModel]
