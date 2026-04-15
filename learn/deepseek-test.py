
# # 定义大模型
# from langchain_openai import ChatOpenAI

# model = ChatOpenAI(
#     model="deepseek-chat",        # 或 deepseek-reasoner（R1推理模型）
#     api_key="sk-3d4558aed3ea4143ba709345860d5a71",
#     base_url="https://api.deepseek.com/v1",
# )


# # 定义消息列表
# from langchain_core.messages import HumanMessage, SystemMessage

# messages = [
#     SystemMessage(content="你是一个翻译官，把用户输入的信息翻译成地道的英语"),
#     HumanMessage(content="阴天你看不见我，天晴你会想起我！"),
# ] 
# # 调用大模型
# result = model.invoke(messages)
# print(result)

# # 解析输出
# from langchain_core.output_parsers import StrOutputParser
# parser = StrOutputParser()
# print(parser.invoke(result))



# 定义大模型
from langchain_openai import ChatOpenAI

# model = ChatOpenAI(
#     model="deepseek-chat",        # 或 deepseek-reasoner（R1推理模型）
#     api_key="sk-3d4558aed3ea4143ba709345860d5a71",
#     base_url="https://api.deepseek.com/v1",
# )

model = ChatOpenAI(
    model="deepseek-chat",
    api_key="sk-3d4558aed3ea4143ba709345860d5a71",
    base_url="https://api.deepseek.com/v1",
    temperature=2,
    # max_tokens=None,
    # timeout=None,
    # max_retries=2,
    # organization="...",
    # other params...
)

# 定义消息列表
from langchain_core.messages import HumanMessage, SystemMessage

# messages = [
#     SystemMessage(content="你是一个翻译官，把用户输入的信息翻译成地道的英语"),
#     HumanMessage(content="阴天你看不见我，天晴你会想起我！"),
# ] 
messages = [
    # SystemMessage(content="你是一个翻译官，把用户输入的信息翻译成地道的英语"),
    HumanMessage(content="一只猴子在_, 用15个字补全这个故事"),
] 
# 定解析输出
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

# 执行链
chain = model | parser
result = chain.invoke(messages)
print(result)


