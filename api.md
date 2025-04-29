# Chat

Types:

```python
from llama_api_client.types import (
    CompletionMessage,
    CreateChatCompletionRequest,
    CreateChatCompletionResponse,
    CreateChatCompletionResponseStreamChunk,
    Message,
    MessageImageContentItem,
    MessageTextContentItem,
    SystemMessage,
    ToolResponseMessage,
    UserMessage,
)
```

## Completions

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/llama_api_client/resources/chat/completions.py">create</a>(\*\*<a href="src/llama_api_client/types/chat/completion_create_params.py">params</a>) -> <a href="./src/llama_api_client/types/create_chat_completion_response.py">CreateChatCompletionResponse</a></code>

# Models

Types:

```python
from llama_api_client.types import LlamaModel, ModelListResponse
```

Methods:

- <code title="get /models/{model}">client.models.<a href="./src/llama_api_client/resources/models.py">retrieve</a>(model) -> <a href="./src/llama_api_client/types/llama_model.py">LlamaModel</a></code>
- <code title="get /models">client.models.<a href="./src/llama_api_client/resources/models.py">list</a>() -> <a href="./src/llama_api_client/types/model_list_response.py">ModelListResponse</a></code>

# Moderations

Types:

```python
from llama_api_client.types import ModerationCreateResponse
```

Methods:

- <code title="post /moderations">client.moderations.<a href="./src/llama_api_client/resources/moderations.py">create</a>(\*\*<a href="src/llama_api_client/types/moderation_create_params.py">params</a>) -> <a href="./src/llama_api_client/types/moderation_create_response.py">ModerationCreateResponse</a></code>
