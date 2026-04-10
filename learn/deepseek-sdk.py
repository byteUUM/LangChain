# from openai import OpenAI
# client = OpenAI(api_key="your-api-key")
# response = client.responses.create(
#     model="gpt-5",
#     input="介绍⼀下你⾃⼰。"
# ) 
# print(response.output_text)

import os
from openai import OpenAI

client = OpenAI(
    api_key='sk-12eb0e810e2744fba7423daa01ed65a3',
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "你是谁？"}],
    stream=False
)

print(response.choices[0].message.content)



