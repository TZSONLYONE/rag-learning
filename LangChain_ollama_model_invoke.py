from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1:7b")

res = model.invoke(input="你是谁呀，能为我做什么")

print(res)