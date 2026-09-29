import asyncio

async def f1():
    print("Task1 started")
    await asyncio.sleep(2)
    print("Task1 completed")

async def f2():
    print("Task2 started")
    await asyncio.sleep(3)
    print("Task2 completed")

async def f3():
    await asyncio.gather(f1(),f2())

asyncio.run(f3())