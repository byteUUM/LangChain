# 提示词传参
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model = "deepseek-chat")

# 方式1
prompt_template = PromptTemplate(
    template="介绍一下{film_name}这部电影",
    input_variables=["film_name"],
)
# 方式2
prompt_template2 = PromptTemplate.from_template("将文本从{language_from}翻译为{language_to}")

# 调用
model.invoke(prompt_template.invoke({"film_name","霸王别姬"})).pretty_print()

# 实例化提示词
print(prompt_template2.invoke({"language_from": "英文", "language_to": "中文"}))

# 聊天信息中的模版

chat_prompt_template = ChatPromptTemplate(
    [
        ("system","将文本从{language_from}翻译为{language_to}"),
        ("user","{text}"),
        # ("ai":"{}"})
    ]
)
# 实例化
messages = chat_prompt_template.invoke(
    {
        "language_from": "英文",
        "language_to": "中文",
        "text": "hi, what is your name?"
    }
)
# # print(messages)
# model.invoke(messages).pretty_print()

# 或
chat_prompt_template = ChatPromptTemplate(
    [
        ("system", "将文本从{language_from}翻译为{language_to}"),
        MessagesPlaceholder("msgs"),  # 消息占位符
        ("user", "{text}"),
        # ("ai", "")
    ]
)

messages_placeholder = [
    HumanMessage(content="hi, what is your name?"),
    AIMessage(content="你好，你叫什么名字？")
]
# 实例化
messages2 = chat_prompt_template.invoke(
    {
        "language_from": "英文",
        "language_to": "中文",
        "text": "hi, what is your age?",
        "msgs": messages_placeholder,
    }
)
print(messages2)

# 在使用时实例化
chain = chat_prompt_template | model
chain.invoke(
    {
        "language_from": "英文",
        "language_to": "中文",
        "text": "hi, what is your age?",
        "msgs": messages_placeholder,
    }
).pretty_print()
