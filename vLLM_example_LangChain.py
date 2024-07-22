import os

from dotenv import load_dotenv

load_dotenv()

from langchain_community.llms import VLLMOpenAI

llm = VLLMOpenAI(
    openai_api_base=f"http://localhost:{os.environ.get('VLLM_PORT')}/v1",
    openai_api_key="EMPTY",
    model_name=f"{os.environ.get('HF_MODEL')}",
    model_kwargs={"stop": ["."]},
)
print(llm.invoke("Rome is"))