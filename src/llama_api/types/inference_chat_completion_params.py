# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "InferenceChatCompletionParamsBase",
    "Message",
    "MessageUserMessage",
    "MessageUserMessageContentUnionMember1",
    "MessageUserMessageContentUnionMember1ImageContentItem",
    "MessageUserMessageContentUnionMember1ImageContentItemImage",
    "MessageUserMessageContentUnionMember1ImageContentItemImageURL",
    "MessageUserMessageContentUnionMember1TextContentItem",
    "MessageSystemMessage",
    "MessageSystemMessageContentUnionMember1",
    "MessageSystemMessageContentUnionMember1ImageContentItem",
    "MessageSystemMessageContentUnionMember1ImageContentItemImage",
    "MessageSystemMessageContentUnionMember1ImageContentItemImageURL",
    "MessageSystemMessageContentUnionMember1TextContentItem",
    "MessageToolResponseMessage",
    "MessageToolResponseMessageContentUnionMember1",
    "MessageToolResponseMessageContentUnionMember1ImageContentItem",
    "MessageToolResponseMessageContentUnionMember1ImageContentItemImage",
    "MessageToolResponseMessageContentUnionMember1ImageContentItemImageURL",
    "MessageToolResponseMessageContentUnionMember1TextContentItem",
    "MessageCompletionMessage",
    "MessageCompletionMessageContentUnionMember1",
    "MessageCompletionMessageContentUnionMember1ImageContentItem",
    "MessageCompletionMessageContentUnionMember1ImageContentItemImage",
    "MessageCompletionMessageContentUnionMember1ImageContentItemImageURL",
    "MessageCompletionMessageContentUnionMember1TextContentItem",
    "MessageCompletionMessageToolCall",
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


class MessageUserMessageContentUnionMember1ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageUserMessageContentUnionMember1ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageUserMessageContentUnionMember1ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageUserMessageContentUnionMember1ImageContentItem(TypedDict, total=False):
    image: Required[MessageUserMessageContentUnionMember1ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageUserMessageContentUnionMember1TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


MessageUserMessageContentUnionMember1: TypeAlias = Union[
    MessageUserMessageContentUnionMember1ImageContentItem, MessageUserMessageContentUnionMember1TextContentItem
]


class MessageUserMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageUserMessageContentUnionMember1]]]
    """The content of the message, which can include text and other media"""

    role: Required[Literal["user"]]
    """Must be "user" to identify this as a user message"""


class MessageSystemMessageContentUnionMember1ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageSystemMessageContentUnionMember1ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageSystemMessageContentUnionMember1ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageSystemMessageContentUnionMember1ImageContentItem(TypedDict, total=False):
    image: Required[MessageSystemMessageContentUnionMember1ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageSystemMessageContentUnionMember1TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


MessageSystemMessageContentUnionMember1: TypeAlias = Union[
    MessageSystemMessageContentUnionMember1ImageContentItem, MessageSystemMessageContentUnionMember1TextContentItem
]


class MessageSystemMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageSystemMessageContentUnionMember1]]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated.
    """

    role: Required[Literal["system"]]
    """Must be "system" to identify this as a system message"""


class MessageToolResponseMessageContentUnionMember1ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageToolResponseMessageContentUnionMember1ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageToolResponseMessageContentUnionMember1ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageToolResponseMessageContentUnionMember1ImageContentItem(TypedDict, total=False):
    image: Required[MessageToolResponseMessageContentUnionMember1ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageToolResponseMessageContentUnionMember1TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


MessageToolResponseMessageContentUnionMember1: TypeAlias = Union[
    MessageToolResponseMessageContentUnionMember1ImageContentItem,
    MessageToolResponseMessageContentUnionMember1TextContentItem,
]


class MessageToolResponseMessage(TypedDict, total=False):
    call_id: Required[str]
    """Unique identifier for the tool call this response is for"""

    content: Required[Union[str, Iterable[MessageToolResponseMessageContentUnionMember1]]]
    """The response content from the tool"""

    role: Required[Literal["tool"]]
    """Must be "tool" to identify this as a tool response"""


class MessageCompletionMessageContentUnionMember1ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageCompletionMessageContentUnionMember1ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageCompletionMessageContentUnionMember1ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageCompletionMessageContentUnionMember1ImageContentItem(TypedDict, total=False):
    image: Required[MessageCompletionMessageContentUnionMember1ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageCompletionMessageContentUnionMember1TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


MessageCompletionMessageContentUnionMember1: TypeAlias = Union[
    MessageCompletionMessageContentUnionMember1ImageContentItem,
    MessageCompletionMessageContentUnionMember1TextContentItem,
]


class MessageCompletionMessageToolCall(TypedDict, total=False):
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


class MessageCompletionMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageCompletionMessageContentUnionMember1]]]
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

    tool_calls: Iterable[MessageCompletionMessageToolCall]
    """List of tool calls. Each tool call is a ToolCall object."""


Message: TypeAlias = Union[
    MessageUserMessage, MessageSystemMessage, MessageToolResponseMessage, MessageCompletionMessage
]


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""


class ResponseFormatJsonSchemaResponseFormat(TypedDict, total=False):
    json_schema: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
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
