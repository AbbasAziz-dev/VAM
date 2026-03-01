import asyncio
import httpx

async def fetch(url):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        return r.json()
    
async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
         ]

    result = await asyncio.gather(*(fetch(u)for u in urls))
    print(result)

asyncio.run(main())
