from typing import Optional, Union
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
import os

model = ChatOpenAI(
    model="gpt-5.5",
    api_key=os.getenv("CHAT_API_KEY"),
    base_url=os.getenv("CHAT_BASE_URL"))


# Pydantic对象
class Joke(BaseModel):
    """给用户讲一个笑话"""
    
    setup: str = Field(description="笑话的开头")
    punchline: str = Field(description="笑话的妙语")
    rating: Optional[int] = Field(default=None, description="1到10分给这个笑话评分")
    
class Response(BaseModel):
    """用对话的方式回应"""
    
    content: str = Field(description="用于对用户查询的会话响应")
    
class FinalResponse(BaseModel):
    """最终的回复，选择合适的输出结构"""
    
    final_output: Union[Joke, Response]

model = model.with_structured_output(FinalResponse)
print(model.invoke("讲一个笑话"))
print(model.invoke("你是什么模型？"))
