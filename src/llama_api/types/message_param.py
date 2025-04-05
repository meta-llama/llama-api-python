# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .user_message_param import UserMessageParam
from .system_message_param import SystemMessageParam
from .completion_message_param import CompletionMessageParam
from .tool_response_message_param import ToolResponseMessageParam

__all__ = ["MessageParam"]

MessageParam: TypeAlias = Union[UserMessageParam, SystemMessageParam, ToolResponseMessageParam, CompletionMessageParam]
