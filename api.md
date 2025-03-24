# Shared Types

```python
from llama_api.types import CompletionMessage, Message, UserMessage
```

# Inference

Types:

```python
from llama_api.types import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletionResponseStreamChunk,
)
```

Methods:

- <code title="post /v1/inference/chat-completion">client.inference.<a href="./src/llama_api/resources/inference.py">chat_completion</a>(\*\*<a href="src/llama_api/types/inference_chat_completion_params.py">params</a>) -> <a href="./src/llama_api/types/chat_completion_response.py">ChatCompletionResponse</a></code>

# Models

Types:

```python
from llama_api.types import Model, ModelListResponse
```

Methods:

- <code title="get /v1/models/{model_id}">client.models.<a href="./src/llama_api/resources/models.py">retrieve</a>(model_id) -> <a href="./src/llama_api/types/model.py">Model</a></code>
- <code title="get /v1/models">client.models.<a href="./src/llama_api/resources/models.py">list</a>() -> <a href="./src/llama_api/types/model_list_response.py">ModelListResponse</a></code>
