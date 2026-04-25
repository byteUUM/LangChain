import os
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

model = ChatOpenAI(model="deepseek-chat")

# 定义工具 
tool = TavilySearch(max_results=3)

# 绑定工具
model_with_tool = model.bind_tools([tool])

# 组织消息
messages = [
    HumanMessage("今天长春天气怎么样?")
]

ai_message = model_with_tool.invoke(messages)
messages.append(ai_message)

for tool_call in ai_message.tool_calls:
    tool_message = tool.invoke(tool_call)
    messages.append(tool_message)

# print(messages)
print(model_with_tool.invoke(messages).content)