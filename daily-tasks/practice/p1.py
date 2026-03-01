import asyncio

async def get_hello(name):
    print('hello')
    await asyncio.sleep(1)
    print(name)

async def get_Id(num):
    print("enter ur id")
    await asyncio.sleep(0.25)
    print(num)

async def main():
    task1= asyncio.create_task(get_hello('abbas'))
    task2 = asyncio.create_task(get_Id(1234))
    task3 = asyncio.create_task(get_hello('aziz'))
    task4 = asyncio.create_task(get_Id(2222))
    
    result = await asyncio.gather(task1 ,task2,task3,task4)

asyncio.run(main())