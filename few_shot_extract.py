import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com"
)

# 要抽取的字段
SCHEMA = ["日期","股票名称","开盘价","收盘价","成交量"]

# 示例： 两条就够，第二条换个币种（人民币/美元），让模型知道单位要一起抽出来
EXAMPLES = [
    {
        "content":"2023-01-10，股市震荡。股票强大科技A股今日开盘价100人民币，一度飙升至105人民币，随后回落至98人民币，最终以102人民币收盘，成交量达到520000。",
        "answers":{"日期": "2023-01-10", "股票名称": "强大科技A股", "开盘价": "100人民币",
                    "收盘价": "102人民币", "成交量": "520000"}
    },
    {
        "content": "2024-05-16，股市利好。股票英伟达美股今日开盘价105美元，一度飙升至109美元，随后回落至100美元，最终以116美元收盘，成交量达到3560000。",
        "answers": {"日期": "2024-05-16", "股票名称": "英伟达美股", "开盘价": "105美元",
                    "收盘价": "116美元", "成交量": "3560000"},
    },
]

# 待抽取：第2句故意没有成交量，用来测试“原文未提及”
questions = [
    "2025-06-16，股市利好。股票传智教育A股今日开盘价66人民币，一度飙升至70人民币，随后回落至65人民币，最终以68人民币收盘，成交量达到123000。",
    "2025-06-06，股市利好。股票黑马程序员A股今日开盘价200人民币，一度飙升至211人民币，随后回落至201人民币，最终以206人民币收盘。",
]

messages = [
    {
        "role":"system",
        "content":f"你帮我完成信息抽取。我给你句子，你抽取{SCHEMA}信息，按JSON字符串输出，"
                  f"如果某些信息不存在，用'原文未提及'表示，请参考如下示例：".replace("SCHEMA", "、".join(SCHEMA)),
    }
]

# 关键：示例变成对话历史
for example in EXAMPLES:
    messages.append({"role":"user","content":example["content"]})
    messages.append({
        "role":"assistant",
        "content":json.dumps(example["answers"],ensure_ascii=False),# ensure_ascii=False 不然中文变 \u4e0a
    })

print(len(messages))

for q in questions:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages + [{"role": "user", "content": f"按照上述的示例，现在抽取这个句子的信息：{q}"}]
    )

    print(response.choices[0].message.content)