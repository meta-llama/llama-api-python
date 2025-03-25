# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..text_content_item_param import TextContentItemParam
from ..image_content_item_param import ImageContentItemParam
from ..reasoning_content_item_param import ReasoningContentItemParam

__all__ = ["CompletionMessage", "Content", "ToolCall"]

Content: TypeAlias = Union[str, ImageContentItemParam, TextContentItemParam, ReasoningContentItemParam]


class ToolCall(TypedDict, total=False):
    arguments: Required[
        Union[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    bool,
                    List[Union[str, float, bool, None]],
                    Dict[str, Union[str, float, bool, None]],
                    None,
                ],
            ],
        ]
    ]

    call_id: Required[str]

    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

    arguments_json: str


class CompletionMessage(TypedDict, total=False):
    content: Required[Content]
    """The content of the model's response"""

    role: Required[Literal["assistant"]]
    """Must be "assistant" to identify this as the model's response"""

    stop_reason: Required[Literal["end_of_turn", "end_of_message", "out_of_tokens"]]
    """Reason why the model stopped generating.

    Options are: - `StopReason.end_of_turn`: The model finished generating the
    entire response. - `StopReason.end_of_message`: The model finished generating
    but generated a partial response -- usually, a tool call. The user may call the
    tool and continue the conversation with the tool's response. -
    `StopReason.out_of_tokens`: The model ran out of token budget.
    """

    tool_calls: Iterable[ToolCall]
    """List of tool calls. Each tool call is a ToolCall object."""
