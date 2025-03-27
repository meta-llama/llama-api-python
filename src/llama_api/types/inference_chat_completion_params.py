# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.message import Message

__all__ = [
    "InferenceChatCompletionParamsBase",
    "Logprobs",
    "ResponseFormat",
    "ResponseFormatJsonSchemaResponseFormat",
    "ResponseFormatGrammarResponseFormat",
    "ToolConfig",
    "Tool",
    "ToolParameters",
    "InferenceChatCompletionParamsNonStreaming",
    "InferenceChatCompletionParamsStreaming",
]


class InferenceChatCompletionParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """List of messages in the conversation"""

    model_id: Required[str]
    """The identifier of the model to use."""

    logprobs: Logprobs
    """If specified, log probabilities for each token position will be returned."""

    max_completion_tokens: int

    repetition_penalty: float

    response_format: ResponseFormat
    """Grammar specification for guided (structured) decoding.

    There are two options: - `ResponseFormat.json_schema`: The grammar is a JSON
    schema. Most providers support this format. - `ResponseFormat.grammar`: The
    grammar is a BNF grammar. This format is more flexible, but not all providers
    support it.
    """

    temperature: float

    tool_choice: Literal["auto", "required", "none"]
    """Whether tool use is required or automatic.

    Defaults to ToolChoice.auto. .. deprecated:: Use tool_config instead.
    """

    tool_config: ToolConfig
    """Configuration for tool use."""

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """Instructs the model how to format tool calls.

    By default, Llama Stack will attempt to use a format that is best adapted to the
    model. - `ToolPromptFormat.json`: The tool calls are formatted as a JSON
    object. - `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
    <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
    are output as Python syntax -- a list of function calls. .. deprecated:: Use
    tool_config instead.
    """

    tools: Iterable[Tool]
    """List of tool definitions available to the model"""

    top_k: int

    top_p: float


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""


class ResponseFormatJsonSchemaResponseFormat(TypedDict, total=False):
    json_schema: Required[object]
    """The JSON schema the response should conform to.

    In a Python SDK, this is often a `pydantic` model.
    """

    type: Required[Literal["json_schema"]]
    """Must be "json_schema" to identify this format type"""


class ResponseFormatGrammarResponseFormat(TypedDict, total=False):
    bnf: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """The BNF grammar specification the response should conform to"""

    type: Required[Literal["grammar"]]
    """Must be "grammar" to identify this format type"""


ResponseFormat: TypeAlias = Union[ResponseFormatJsonSchemaResponseFormat, ResponseFormatGrammarResponseFormat]


class ToolConfig(TypedDict, total=False):
    system_message_behavior: Literal["append", "replace"]
    """Config for how to override the default system prompt.

    - `SystemMessageBehavior.append`: Appends the provided system message to the
      default system prompt. - `SystemMessageBehavior.replace`: Replaces the default
      system prompt with the provided system message. The system message can include
      the string '{{function_definitions}}' to indicate where the function
      definitions should be inserted.
    """

    tool_choice: Union[Literal["auto", "required", "none"], str]
    """Whether tool use is automatic, required, or none.

    Can also specify a tool name to use a specific tool. Defaults to
    ToolChoice.auto.
    """

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """Instructs the model how to format tool calls.

    By default, Llama Stack will attempt to use a format that is best adapted to the
    model. - `ToolPromptFormat.json`: The tool calls are formatted as a JSON
    object. - `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
    <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
    are output as Python syntax -- a list of function calls.
    """


class ToolParameters(TypedDict, total=False):
    param_type: Required[str]

    default: Union[bool, float, str, Iterable[object], object, None]

    description: str

    required: bool


class Tool(TypedDict, total=False):
    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

    description: str

    parameters: Dict[str, ToolParameters]


class InferenceChatCompletionParamsNonStreaming(InferenceChatCompletionParamsBase, total=False):
    stream: Literal[False]
    """If True, generate an SSE event stream of the response. Defaults to False."""


class InferenceChatCompletionParamsStreaming(InferenceChatCompletionParamsBase):
    stream: Required[Literal[True]]
    """If True, generate an SSE event stream of the response. Defaults to False."""


InferenceChatCompletionParams = Union[InferenceChatCompletionParamsNonStreaming, InferenceChatCompletionParamsStreaming]
