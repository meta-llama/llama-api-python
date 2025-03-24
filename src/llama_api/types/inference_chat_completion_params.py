# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "InferenceChatCompletionParamsBase",
    "Message",
    "MessageUserMessage",
    "MessageUserMessageContent",
    "MessageUserMessageContentImageContentItem",
    "MessageUserMessageContentImageContentItemImage",
    "MessageUserMessageContentImageContentItemImageURL",
    "MessageUserMessageContentTextContentItem",
    "MessageUserMessageContentUnionMember3",
    "MessageUserMessageContentUnionMember3ImageContentItem",
    "MessageUserMessageContentUnionMember3ImageContentItemImage",
    "MessageUserMessageContentUnionMember3ImageContentItemImageURL",
    "MessageUserMessageContentUnionMember3TextContentItem",
    "MessageUserMessageContext",
    "MessageUserMessageContextImageContentItem",
    "MessageUserMessageContextImageContentItemImage",
    "MessageUserMessageContextImageContentItemImageURL",
    "MessageUserMessageContextTextContentItem",
    "MessageUserMessageContextUnionMember3",
    "MessageUserMessageContextUnionMember3ImageContentItem",
    "MessageUserMessageContextUnionMember3ImageContentItemImage",
    "MessageUserMessageContextUnionMember3ImageContentItemImageURL",
    "MessageUserMessageContextUnionMember3TextContentItem",
    "MessageSystemMessage",
    "MessageSystemMessageContent",
    "MessageSystemMessageContentImageContentItem",
    "MessageSystemMessageContentImageContentItemImage",
    "MessageSystemMessageContentImageContentItemImageURL",
    "MessageSystemMessageContentTextContentItem",
    "MessageSystemMessageContentUnionMember3",
    "MessageSystemMessageContentUnionMember3ImageContentItem",
    "MessageSystemMessageContentUnionMember3ImageContentItemImage",
    "MessageSystemMessageContentUnionMember3ImageContentItemImageURL",
    "MessageSystemMessageContentUnionMember3TextContentItem",
    "MessageToolResponseMessage",
    "MessageToolResponseMessageContent",
    "MessageToolResponseMessageContentImageContentItem",
    "MessageToolResponseMessageContentImageContentItemImage",
    "MessageToolResponseMessageContentImageContentItemImageURL",
    "MessageToolResponseMessageContentTextContentItem",
    "MessageToolResponseMessageContentUnionMember3",
    "MessageToolResponseMessageContentUnionMember3ImageContentItem",
    "MessageToolResponseMessageContentUnionMember3ImageContentItemImage",
    "MessageToolResponseMessageContentUnionMember3ImageContentItemImageURL",
    "MessageToolResponseMessageContentUnionMember3TextContentItem",
    "MessageCompletionMessage",
    "MessageCompletionMessageContent",
    "MessageCompletionMessageContentImageContentItem",
    "MessageCompletionMessageContentImageContentItemImage",
    "MessageCompletionMessageContentImageContentItemImageURL",
    "MessageCompletionMessageContentTextContentItem",
    "MessageCompletionMessageContentUnionMember3",
    "MessageCompletionMessageContentUnionMember3ImageContentItem",
    "MessageCompletionMessageContentUnionMember3ImageContentItemImage",
    "MessageCompletionMessageContentUnionMember3ImageContentItemImageURL",
    "MessageCompletionMessageContentUnionMember3TextContentItem",
    "MessageCompletionMessageToolCall",
    "Logprobs",
    "ResponseFormat",
    "ResponseFormatJsonSchemaResponseFormat",
    "ResponseFormatGrammarResponseFormat",
    "SamplingParams",
    "SamplingParamsStrategy",
    "SamplingParamsStrategyGreedySamplingStrategy",
    "SamplingParamsStrategyTopPSamplingStrategy",
    "SamplingParamsStrategyTopKSamplingStrategy",
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

    response_format: ResponseFormat
    """Grammar specification for guided (structured) decoding.

    There are two options: - `ResponseFormat.json_schema`: The grammar is a JSON
    schema. Most providers support this format. - `ResponseFormat.grammar`: The
    grammar is a BNF grammar. This format is more flexible, but not all providers
    support it.
    """

    sampling_params: SamplingParams
    """Parameters to control the sampling strategy"""

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


class MessageUserMessageContentImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageUserMessageContentImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageUserMessageContentImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageUserMessageContentImageContentItem(TypedDict, total=False):
    image: Required[MessageUserMessageContentImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageUserMessageContentTextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class MessageUserMessageContentUnionMember3ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageUserMessageContentUnionMember3ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageUserMessageContentUnionMember3ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageUserMessageContentUnionMember3ImageContentItem(TypedDict, total=False):
    image: Required[MessageUserMessageContentUnionMember3ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageUserMessageContentUnionMember3TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


MessageUserMessageContentUnionMember3: TypeAlias = Union[
    MessageUserMessageContentUnionMember3ImageContentItem, MessageUserMessageContentUnionMember3TextContentItem
]

MessageUserMessageContent: TypeAlias = Union[
    str,
    MessageUserMessageContentImageContentItem,
    MessageUserMessageContentTextContentItem,
    Iterable[MessageUserMessageContentUnionMember3],
]


class MessageUserMessageContextImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageUserMessageContextImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageUserMessageContextImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageUserMessageContextImageContentItem(TypedDict, total=False):
    image: Required[MessageUserMessageContextImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageUserMessageContextTextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class MessageUserMessageContextUnionMember3ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageUserMessageContextUnionMember3ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageUserMessageContextUnionMember3ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageUserMessageContextUnionMember3ImageContentItem(TypedDict, total=False):
    image: Required[MessageUserMessageContextUnionMember3ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageUserMessageContextUnionMember3TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


MessageUserMessageContextUnionMember3: TypeAlias = Union[
    MessageUserMessageContextUnionMember3ImageContentItem, MessageUserMessageContextUnionMember3TextContentItem
]

MessageUserMessageContext: TypeAlias = Union[
    str,
    MessageUserMessageContextImageContentItem,
    MessageUserMessageContextTextContentItem,
    Iterable[MessageUserMessageContextUnionMember3],
]


class MessageUserMessage(TypedDict, total=False):
    content: Required[MessageUserMessageContent]
    """The content of the message, which can include text and other media"""

    role: Required[Literal["user"]]
    """Must be "user" to identify this as a user message"""

    context: MessageUserMessageContext
    """This field is used to pass RAG context."""


class MessageSystemMessageContentImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageSystemMessageContentImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageSystemMessageContentImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageSystemMessageContentImageContentItem(TypedDict, total=False):
    image: Required[MessageSystemMessageContentImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageSystemMessageContentTextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class MessageSystemMessageContentUnionMember3ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageSystemMessageContentUnionMember3ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageSystemMessageContentUnionMember3ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageSystemMessageContentUnionMember3ImageContentItem(TypedDict, total=False):
    image: Required[MessageSystemMessageContentUnionMember3ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageSystemMessageContentUnionMember3TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


MessageSystemMessageContentUnionMember3: TypeAlias = Union[
    MessageSystemMessageContentUnionMember3ImageContentItem, MessageSystemMessageContentUnionMember3TextContentItem
]

MessageSystemMessageContent: TypeAlias = Union[
    str,
    MessageSystemMessageContentImageContentItem,
    MessageSystemMessageContentTextContentItem,
    Iterable[MessageSystemMessageContentUnionMember3],
]


class MessageSystemMessage(TypedDict, total=False):
    content: Required[MessageSystemMessageContent]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated.
    """

    role: Required[Literal["system"]]
    """Must be "system" to identify this as a system message"""


class MessageToolResponseMessageContentImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageToolResponseMessageContentImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageToolResponseMessageContentImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageToolResponseMessageContentImageContentItem(TypedDict, total=False):
    image: Required[MessageToolResponseMessageContentImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageToolResponseMessageContentTextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class MessageToolResponseMessageContentUnionMember3ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageToolResponseMessageContentUnionMember3ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageToolResponseMessageContentUnionMember3ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageToolResponseMessageContentUnionMember3ImageContentItem(TypedDict, total=False):
    image: Required[MessageToolResponseMessageContentUnionMember3ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageToolResponseMessageContentUnionMember3TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


MessageToolResponseMessageContentUnionMember3: TypeAlias = Union[
    MessageToolResponseMessageContentUnionMember3ImageContentItem,
    MessageToolResponseMessageContentUnionMember3TextContentItem,
]

MessageToolResponseMessageContent: TypeAlias = Union[
    str,
    MessageToolResponseMessageContentImageContentItem,
    MessageToolResponseMessageContentTextContentItem,
    Iterable[MessageToolResponseMessageContentUnionMember3],
]


class MessageToolResponseMessage(TypedDict, total=False):
    call_id: Required[str]
    """Unique identifier for the tool call this response is for"""

    content: Required[MessageToolResponseMessageContent]
    """The response content from the tool"""

    role: Required[Literal["tool"]]
    """Must be "tool" to identify this as a tool response"""


class MessageCompletionMessageContentImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageCompletionMessageContentImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageCompletionMessageContentImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageCompletionMessageContentImageContentItem(TypedDict, total=False):
    image: Required[MessageCompletionMessageContentImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageCompletionMessageContentTextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


class MessageCompletionMessageContentUnionMember3ImageContentItemImageURL(TypedDict, total=False):
    uri: Required[str]


class MessageCompletionMessageContentUnionMember3ImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: MessageCompletionMessageContentUnionMember3ImageContentItemImageURL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class MessageCompletionMessageContentUnionMember3ImageContentItem(TypedDict, total=False):
    image: Required[MessageCompletionMessageContentUnionMember3ImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class MessageCompletionMessageContentUnionMember3TextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


MessageCompletionMessageContentUnionMember3: TypeAlias = Union[
    MessageCompletionMessageContentUnionMember3ImageContentItem,
    MessageCompletionMessageContentUnionMember3TextContentItem,
]

MessageCompletionMessageContent: TypeAlias = Union[
    str,
    MessageCompletionMessageContentImageContentItem,
    MessageCompletionMessageContentTextContentItem,
    Iterable[MessageCompletionMessageContentUnionMember3],
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
    content: Required[MessageCompletionMessageContent]
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


class SamplingParamsStrategyGreedySamplingStrategy(TypedDict, total=False):
    type: Required[Literal["greedy"]]


class SamplingParamsStrategyTopPSamplingStrategy(TypedDict, total=False):
    type: Required[Literal["top_p"]]

    temperature: float

    top_p: float


class SamplingParamsStrategyTopKSamplingStrategy(TypedDict, total=False):
    top_k: Required[int]

    type: Required[Literal["top_k"]]


SamplingParamsStrategy: TypeAlias = Union[
    SamplingParamsStrategyGreedySamplingStrategy,
    SamplingParamsStrategyTopPSamplingStrategy,
    SamplingParamsStrategyTopKSamplingStrategy,
]


class SamplingParams(TypedDict, total=False):
    strategy: Required[SamplingParamsStrategy]

    max_tokens: int

    repetition_penalty: float


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
