from langchain_deepseek import ChatDeepSeek

model = ChatDeepSeek(model="deepseek-chat")

messages = [
    ("system","你是一名边塞诗人。"),
    ("human","写一首唐诗。"),
    ("ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    ("human","按照你上一个回复的格式，再写一首唐诗")
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk.content,end="",flush=True)