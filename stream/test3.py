from langchain_openai import ChatOpenAI
from typing import Iterator, List
from langchain_core.output_parsers import StrOutputParser
import os

# 定义大模型
# model = ChatOpenAI(
#     model="gpt-5.5",
#     api_key=os.getenv("CHAT_API_KEY"),
#     base_url=os.getenv("CHAT_BASE_URL"))

model = ChatOpenAI(model="deepseek-v4-pro")

# 组件2输出解析器
parser = StrOutputParser()

# 自定义生成器
def split_into_list(input: Iterator[str]) -> Iterator[List[str]]:
    buffer = ""
    for chunk in input:
        buffer += chunk
        while "。" in buffer:
            stop_index = buffer.index("。")
            yield [buffer[: stop_index].strip()]
            buffer = buffer[stop_index+1 :]
    yield [buffer.strip()]
    
# 定义链
chain = model | parser | split_into_list

for chunk in chain.stream("写一首关于夏天的诗"):
    print(chunk)
