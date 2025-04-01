# Chat

Types:

```python
from llama_api.types import (
    CreateChatCompletionRequest,
    CreateChatCompletionResponse,
    CreateChatCompletionResponseStreamChunk,
)
```

## Completions

Methods:

- <code title="post /v1/chat/completions">client.chat.completions.<a href="./src/llama_api/resources/chat/completions.py">create</a>(\*\*<a href="src/llama_api/types/chat/completion_create_params.py">params</a>) -> <a href="./src/llama_api/types/create_chat_completion_response.py">CreateChatCompletionResponse</a></code>

# Models

Types:

```python
from llama_api.types import AIModel, ModelListResponse
```

Methods:

- <code title="get /v1/models/{model}">client.models.<a href="./src/llama_api/resources/models.py">retrieve</a>(model) -> <a href="./src/llama_api/types/ai_model.py">AIModel</a></code>
- <code title="get /v1/models">client.models.<a href="./src/llama_api/resources/models.py">list</a>() -> <a href="./src/llama_api/types/model_list_response.py">ModelListResponse</a></code>
