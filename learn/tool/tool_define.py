from langchain_core.tools import tool
from pydantic import BaseModel, Field
from typing_extensions import Annotated

# 定义工具
# tool
# 示例1:
@tool
def add1(a: int, b: int) -> int:
    """两数相加
    Args:
        a: 第一个整数
        b: 第二个整数
    """
    return a + b
    
# 示例2:
class AddInput(BaseModel):
    """两数相加"""
    
    a: int = Field(..., description="第一个整数")
    b: int = Field(..., description="第二个整数")
    
    
@tool(args_schema=AddInput)
def add2(a: int, b: int) -> int:
    return a+b

# 示例3:
def add3(
    a: Annotated[int, ..., "第一个整数"],
    b: Annotated[int, ..., "第二个整数"],
)-> int:
    """两数相加
    
    Args:
        a: 第一个整数
        b: 第二个整数
    """
    return a+b
    
print(add1.invoke({"a":2,"b":3}))
print(add1.name)
print(add1.description)
print(add1.args)