import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=f"http://localhost:{os.environ.get('VLLM_PORT')}/v1",
    api_key="EMPTY",
)

completion = client.chat.completions.create(
  model=f"{os.environ.get('HF_MODEL')}",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)