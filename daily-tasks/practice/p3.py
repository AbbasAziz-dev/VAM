import asyncio


sem = asyncio.Semaphore(2)

async def limited_task(n):
    async with sem:
        print("start",n)
        await asyncio.sleep(0.5)
        print("exit")

async def main():
    await asyncio.gather(
        limited_task(1),
        limited_task(2),
        limited_task(3),
        limited_task(4),
    )

asyncio.run(main())





