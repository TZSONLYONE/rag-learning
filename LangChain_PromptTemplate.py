from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

prompt_template =PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字，简单回答。"
)

model = ChatDeepSeek(model="deepseek-chat")

chain = prompt_template | model

res =chain.invoke(input={"lastname":"唐","gender":"男孩"})
print(res.content)