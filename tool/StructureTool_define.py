from typing import Tuple, List
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

# 示例1:
def add1(a:int, b:int) -> int:
    """两数相加"""
    return a+b

add_tool = StructuredTool.from_function(func=add1)

# 示例2:
class AddInput(BaseModel):
    a:int = Field(...,description="第一个整数"),
    b:int = Field(...,description="第二个整数"),
    
def add2(a:int, b:int) -> int:
    return a+b

add2_tool = StructuredTool.from_function(
    func=add2,
    name="Add",             #重新给工具起名
    description="两数相加",  #工具功能描述
    args_schema=AddInput,   #工具参数
)

# 示例3:
class Add3Input(BaseModel):
    a:int = Field(...,description="第一个整数"),
    b:int = Field(...,description="第二个整数"),
    
def add3(a:int, b:int) -> int:
    nums = [a,b]
    content = f"{nums}相加的结果是{a+b}"
    return content, nums

add3_tool = StructuredTool.from_function(
    func=add3,
    name="Add3",
    description="两数相加",
    args_schema=Add3Input,
    response_format="content_and_artifact"
)

# 模拟大模型调用姿势
print(add3_tool.invoke(
    {
        "name":"add3",
        "args":{"a":3,"b":4},
        "type":"tool_call", #让模型调用工具来完成
        "id":"11",         #让模型知道返回的结果是哪一次调用
    }
))

print(add_tool.invoke({"a":2, "b":5}))
print(add_tool.name)
print(add_tool.description)
print(add_tool.args)
