from typing import Optional, List, TypedDict
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing_extensions import Annotated
import os
model = ChatOpenAI(
    model="gpt-5.5",
    api_key=os.getenv("CHAT_API_KEY"),
    base_url=os.getenv("CHAT_BASE_URL")
)

# TypedDict
class Joke(TypedDict):
    """给用户讲一个笑话"""
    
    setup: Annotated[str,...,"这个笑话的开头"]
    punchline: Annotated[str,...,"这个笑话的妙语"]
    rating: Annotated[Optional[int],...,"1到10分给这个笑话一个评分"]

model = model.with_structured_output(Joke, include_raw=True)
print(model.invoke("讲一个笑话"))