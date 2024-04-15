# vLLM-Mistral
Quick tuto to deploy a vLLM instance using the Mistral Docker Image.

## Deploy it!
```bash
docker compose up --build

# Run these steps if you run into:
--> [AttributeError: 'CompletionResponse' object has no attribute 'model_dump'] <--

docker exec -it mistral-src_instance pip uninstall pydantic  # 2x times if necessary!
docker exec -it mistral-src_instance pip install pydantic
docker compose up -d
```

## Test it!
### With Curls...
```shell
curl http://localhost:11435/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "prompt": "San Francisco is a",
        "max_tokens": 7,
        "temperature": 0
    }'
```

```shell
curl http://localhost:11435/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
    }'
```


### With Python...
```shell
python -u -m vllm.entrypoints.openai.api_server \
       --host 0.0.0.0 \
       --port 11435 \
       --model mistralai/Mistral-7B-Instruct-v0.2 \
       --max-model-len 20000
```
