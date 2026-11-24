from  langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_deepseek import ChatDeepSeek

example_template = PromptTemplate.from_template("单词：{word},反义词：{antonym}")

example_date = [
    {"word":"大","antonym":"小"},
    {"word":"上","antonym":"下"}
]

few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,
    examples=example_date,
    prefix="告知我单词的反义词，我提供如下的示例：",
    suffix="基于前面的示例告知我，{input_word}的反义词是？",
    input_variables=['input_word']
)

prompt_text = few_shot_template.invoke(input={"input_word":"右"}).to_string()
print(prompt_text)

model = ChatDeepSeek(model="deepseek-chat")

print(model.invoke(input=prompt_text))