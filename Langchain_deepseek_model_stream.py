from langchain_deepseek import ChatDeepSeek

models = ChatDeepSeek(model = "deepseek-chat")

res = models.stream(input="你是谁呀能做什么？用500字介绍")

for chunk in res:
    print(chunk.content,end="",flush=True)

