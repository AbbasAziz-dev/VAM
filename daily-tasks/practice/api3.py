import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1)
)
async def fetch_async():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpstat.us/500")
        response.raise_for_status()
        return response.text