from langchain.chat_models import init_chat_model

# 定义模型
model = init_chat_model(model = "deepseek-chat",api_key = "sk-c73b3bca388643ebabbbfe3d5093ed81",
        model_provider="deepseek")


#调用并输出
print(model.invoke("你是谁？"))
