from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="deepseek-chat")

# model.invoke("我是阿花，你好！").pretty_print()
# model.invoke("你知道我是谁吗").pretty_print()

# message = [
#     HumanMessage(content="我是阿花，你好！"),
#     AIMessage(content="你好，阿花！很高兴认识你！"),#模拟大模型回复
#     HumanMessage(content="你知道我是谁吗？")
# ]
# model.invoke(message).pretty_print()
store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
        
with_history_message_model = RunnableWithMessageHistory(model, get_session_history)

# 创建会话实例
config = {"configurable":{"session_id":"1"}}

with_history_message_model.invoke(
    [HumanMessage(content="我是阿康，你好")],
    config=config,
).pretty_print()

with_history_message_model.invoke(
    [HumanMessage(content="你知道我是谁吗？")],
    config = config,
).pretty_print()