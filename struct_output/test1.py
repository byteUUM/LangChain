from typing import Optional, List, TypedDict
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
import os
# model = ChatOpenAI(model="deepseek-chat")
# print(model.invoke("讲一个笑话").content)

model = ChatOpenAI(
    model="gpt-5.5",
    api_key=os.getenv("CHAT_API_KEY"),
    base_url=os.getenv("CHAT_BASE_URL"))

# print(model.invoke("讲一个笑话").content)

# Pydantic对象
class Joke(BaseModel):
    """给用户讲一个笑话"""
    
    setup: str = Field(description="笑话的开头")
    punchline: str = Field(description="笑话的妙语")
    rating: Optional[int] = Field(default=None, description="1到10分给这个笑话评分")
    
model_with_structured2 = model.with_structured_output(Joke)
print(model_with_structured2.invoke("讲一个笑话"))
