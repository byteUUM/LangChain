import asyncio

async def boil_water_aync():
    print("开始烧水...")
    await asyncio.sleep(5)
    print("烧水完成！")

async def send_message_async():
    print("开始洗衣服...")
    await asyncio.sleep(2)
    print("洗衣服完成！")
    
async def main():
    task1 = asyncio.create_task(boil_water_aync())
    task2 = asyncio.create_task(send_message_async())
    await task1
    await task2
    
asyncio.run(main())    