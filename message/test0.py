from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
model = ChatOpenAI(model="deepseek-chat")

message = [
    SystemMessage(content="你是一个翻译官，需要将用户输入的内容翻译成英文"),
    HumanMessage(content="阴天你看不见我，晴天你会想起我!")
]


result = model.invoke(message)
result.pretty_print()
result.pretty_repr()
result.pretty_repr(html=True)
result.text()

# print(f"消息内容:{result.content}")
# print(f"附加数据:{result.additional_kwargs}")
# print(f"响应元数据:{result.response_metadata}")
# print(f"消息类型:{result.type}")
# print(f"消息名称:{result.name}")
# print(f"消息唯一ID:{result.id}")
