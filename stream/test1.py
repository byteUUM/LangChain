from langchain_openai import ChatOpenAI
import asyncio

model = ChatOpenAI(model="deepseek-v4-pro")
prompt = "写一篇关于夏天在作文，800字左右"

for chunk in model.stream(prompt):
    print(chunk.content,end="",flush=True)
    
# 异步输出
async def async_stream():
    async for chunk in model.astream(prompt):
        print(chunk.content,end="",flush=True)
        
asyncio.run(async_stream())