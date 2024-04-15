from langchain_community.llms import VLLMOpenAI

llm = VLLMOpenAI(
    openai_api_key="EMPTY",
    openai_api_base="http://10.1.246.1:11435/v1",
    model_name="mistralai/Mistral-7B-Instruct-v0.2",
    # model_kwargs={"stop": ["."]},
    # model_kwargs=model_kwargs,
)
# print(llm.invoke("Rome is"))
prompt = "<s>[INST]Tell me who you are. Answer in less than 50 words.[/INST]"

pred = llm.predict(
    prompt,
)
print(pred)
