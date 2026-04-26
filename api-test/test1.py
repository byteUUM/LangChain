# from langchain_openai import ChatOpenAI
# model = ChatOpenAI(model="deepseek-chat")

# # 定义消息列表
# from langchain_core.messages import HumanMessage, SystemMessage
# messages = [
#     SystemMessage(content="你是一个翻译官，把用户输入的信息翻译成地道的英语"),
#     HumanMessage(content="阴天你看不见我，天晴你会想起我！"),
# ]

# # 定解析输出
# from langchain_core.output_parsers import StrOutputParser
# parser = StrOutputParser()

# # 执行链
# chain = model | parser
# result = chain.invoke(messages)
# print(result)


# from langchain_openai import ChatOpenAI
# model1 = ChatOpenAI(model="deepseek-chat",temperature=0.0)
# model2 = ChatOpenAI(model="deepseek-chat",temperature=1.0)
# model3 = ChatOpenAI(model="deepseek-chat",temperature=2.0)

# from langchain_core.messages import HumanMessage, SystemMessage
# messages = [
#     SystemMessage(content="给你一段话，补全故事"),
#     HumanMessage(content="一只小狗在__, 用15个字补全这个故事"),
# ] 
# print(model1.invoke(messages).content)
# print(model2.invoke(messages).content)
# print(model3.invoke(messages).content)

# from langchain.chat_models import init_chat_model
# model = init_chat_model(model="deepseek-v4-flash")
# print(model.invoke("你是谁？").content)

from langchain.chat_models import init_chat_model
model = init_chat_model(
    model="deepseek-chat",
    max_tokens = 500,
    temperature = 2,
    configurable_fields = ("max_tokens","temperature"),
    config_prefix = "first"
)

print(model.invoke(
    input="你是谁？",
    config={
        "configurable":{
            "first_max_tokens":10,
            "first_temperature":0.7
        }
    }
).content)