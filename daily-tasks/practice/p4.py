import asyncio

async def foo(num):
    print("hii")
    await asyncio.sleep(5)
    print(num)


async def main():
    try:
        await asyncio.wait_for(foo(121), timeout=2)
    except asyncio.TimeoutError:
        print("Timed out")
asyncio.run(main())