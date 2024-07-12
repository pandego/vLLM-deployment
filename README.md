# vLLM Instance Deployment
## Intro
Quick tuto to deploy a vLLM instance using the [Official Docker Image](https://hub.docker.com/r/vllm/vllm-openai/tags).

## Pre-requisits
- Conda
- GPU (Nvidia)

# Environment
This was testing on **Ubuntu only**, but it should work well on **MacOS** and **Windows WSL**.
- Clone this repo:
    ```bash
    git clone https://github.com/pandego/vLLM-deployment.git
    cd vllm
    ```

- Setup the environment:
    ```bash
    conda env create -f environment.yml
    conda activate vllm
    ```

- Install dependencies:
    ```bash
    poetry install --no-root
    ```

## Deploy it...
### ... `docker compose` it!
#### The `.env` File
- Let's keep things clean. So first, copy `default.env` into `.env`:
  ```bash
  mv default.env .env
  ```
- You might need to edit the contents of the `.env` file with your HuggingFace Token

- Deploy you container:
    ```bash
    docker compose up --build -d
    ```
### ... using Python

```bash
python -m vllm.entrypoints.openai.api_server \
            --model NousResearch/Meta-Llama-3-8B-Instruct --dtype auto --api-key token-abc123
```

## Test it...
### ... `curl` it!
- You can run the following command to test the vLLM instance. Be sure to change the `model` if necessary:
    - Using `completions`:
        ```bash
        curl http://localhost:11435/v1/completions \
            -H "Content-Type: application/json" \
            -d '{
                "model": "mistralai/Mistral-7B-Instruct-v0.2",
                "prompt": "San Francisco is a",
                "max_tokens": 7,
                "temperature": 0
            }'
        ```
    - Using `chat/completions`:
        ```bash
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


### ... using  ***Python***!
- 
    ```bash
    python -u -m vllm.entrypoints.openai.api_server \
        --host 0.0.0.0 \
        --port 11435 \
        --model mistralai/Mistral-7B-Instruct-v0.2 \
        --max-model-len 30000
    ```


## Need more info?
- You can check some more arguments in the `helper_args.json` file.
- Find more info in the vLLM documentaion [here](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html).