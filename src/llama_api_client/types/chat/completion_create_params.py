# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..message_param import MessageParam

__all__ = [
    "CompletionCreateParamsBase",
    "ResponseFormat",
    "ResponseFormatJsonSchemaResponseFormat",
    "ResponseFormatJsonSchemaResponseFormatJsonSchema",
    "ResponseFormatTextResponseFormat",
    "ToolChoice",
    "ToolChoiceChatCompletionNamedToolChoice",
    "ToolChoiceChatCompletionNamedToolChoiceFunction",
    "Tool",
    "ToolFunction",
    "CompletionCreateParamsNonStreaming",
    "CompletionCreateParamsStreaming",
]


class CompletionCreateParamsBase(TypedDict, total=False):
    messages: Required[Iterable[MessageParam]]
    """List of messages in the conversation."""

    model: Required[str]
    """The identifier of the model to use."""

    max_completion_tokens: int
    """The maximum number of tokens to generate."""

    repetition_penalty: float
    """Controls the likelyhood and generating repetitive responses."""

    response_format: ResponseFormat
    """
    An object specifying the format that the model must output. Setting to
    `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs
    which ensures the model will match your supplied JSON schema. If not specified,
    the default is {"type": "text"}, and model will return a free-form text
    response.
    """

    temperature: float
    """Controls randomness of the response by setting a temperature.

    Higher value leads to more creative responses. Lower values will make the
    response more focused and deterministic.
    """

    tool_choice: ToolChoice
    """
    Controls which (if any) tool is called by the model. `none` means the model will
    not call any tool and instead generates a message. `auto` means the model can
    pick between generating a message or calling one or more tools. `required` means
    the model must call one or more tools. Specifying a particular tool via
    `{"type": "function", "function": {"name": "my_function"}}` forces the model to
    call that tool.

    `none` is the default when no tools are present. `auto` is the default if tools
    are present.
    """

    tools: Iterable[Tool]
    """List of tool definitions available to the model"""

    top_k: int
    """Only sample from the top K options for each subsequent token."""

    top_p: float
    """
    Controls diversity of the response by setting a probability threshold when
    choosing the next token.
    """

    user: str
    """
    A unique identifier representing your application end-user for monitoring abuse.
    """


class ResponseFormatJsonSchemaResponseFormatJsonSchema(TypedDict, total=False):
    name: Required[str]
    """The name of the response format."""

    schema: Required[object]
    """The JSON schema the response should conform to.

    In a Python SDK, this is often a `pydantic` model.
    """


class ResponseFormatJsonSchemaResponseFormat(TypedDict, total=False):
    json_schema: Required[ResponseFormatJsonSchemaResponseFormatJsonSchema]
    """The JSON schema the response should conform to."""

    type: Required[Literal["json_schema"]]
    """The type of response format being defined. Always `json_schema`."""


class ResponseFormatTextResponseFormat(TypedDict, total=False):
    type: Required[Literal["text"]]
    """The type of response format being defined. Always `text`."""


ResponseFormat: TypeAlias = Union[ResponseFormatJsonSchemaResponseFormat, ResponseFormatTextResponseFormat]


class ToolChoiceChatCompletionNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""


class ToolChoiceChatCompletionNamedToolChoice(TypedDict, total=False):
    function: Required[ToolChoiceChatCompletionNamedToolChoiceFunction]

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


ToolChoice: TypeAlias = Union[Literal["none", "auto", "required"], ToolChoiceChatCompletionNamedToolChoice]


class ToolFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Dict[str, object]
    """The parameters the functions accepts, described as a JSON Schema object.

    Omitting `parameters` defines a function with an empty parameter list.
    """

    strict: bool
    """Whether to enable strict schema adherence when generating the function call.

    If set to true, the model will follow the exact schema defined in the
    `parameters` field. Only a subset of JSON Schema is supported when `strict` is
    `true`. Learn more about Structured Outputs in the
    [function calling guide](docs/guides/function-calling).
    """


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Literal[False]
    """If True, generate an SSE event stream of the response. Defaults to False."""


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """If True, generate an SSE event stream of the response. Defaults to False."""


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
