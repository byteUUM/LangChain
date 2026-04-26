from langchain.chat_models import init_chat_model

# # 定义模型
# model = init_chat_model(model = "deepseek-chat",api_key = "sk-c73b3bca388643ebabbbfe3d5093ed81",
#         model_provider="deepseek")

model = init_chat_model(
    model_provider="deepseek", 
    temperature=0.7,
    max_tokens=10,
    configurable_fields=("max_tokens", "model"),
    config_prefix="first",
)

# # 组织消息
# message = [
#     SystemMessage(content="给你一段话，补全故事"),
#     HumanMessage(conetent="一头牛在菜地里__")
# ]

message = "你是谁？"

result = model.invoke(
    input=message,
    config={
    "configurable":{
        "first_model":"deepseek-chat",
        "first_max_tokens":100,
        }
    })

#调用并输出
print(result)
