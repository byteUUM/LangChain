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

json_schema = {
    "title": "joke",
    "description": "给用户讲一个笑话。",
    "type": "object",
    "properties": {
        "setup": {
            "type": "string",
            "description": "这个笑话的开头",
        },
        "punchline": {
            "type": "string",
            "description": "这个笑话的妙语",
        },
        "rating": {
            "type": "integer",
            "description": "从1到10分，给这个笑话评分",
            "default": None,
        },
    },
    "required": ["setup", "punchline"],
}

model = model.with_structured_output(json_schema)
print(model.invoke("讲一个笑话"))