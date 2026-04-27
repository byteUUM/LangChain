
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from typing_extensions import Annotated

@tool
def add(a:int, b:int) -> int:
    """两数相加
    
    Args:
        a:第一个整数
        b:第二个整数
    """
    return a+b

@tool
def multiply(
    a: Annotated[int, ..., "第一个整数"],
    b: Annotated[int, ..., "第二个整数"],
) -> int:
    """两数相乘"""
    return a*b

model = ChatOpenAI(model="deepseek-chat")
# 工具绑定
tools = [add, multiply]
model_with_tools = model.bind_tools(tools = tools)
# 调用工具
msg = model_with_tools.invoke("45乘2等于多少？") # 没有真正调用工具，只是匹配工具？

print(model_with_tools.invoke("45乘2等于多少？"))
print(multiply.invoke(msg.tool_calls[0]).content)

# # 定义消息列表
# message = [
#     HumanMessage("50加4等于多少? 7乘11等于多少?")
# ]
# ai_msg = model_with_tools.invoke(message)
# message.append(ai_msg)

# for tool_call in ai_msg.tool_calls:
#     selected_tool = {"add":add, "multiply":multiply}[tool_call["name"].lower()] #名称匹配tool忽略大小写
#     tool_msg = selected_tool.invoke(tool_call) #执行tool
#     message.append(tool_msg)
    
# print(message)
# print(model.invoke(message).content)
# print(model_with_tools.invoke(message).content)

