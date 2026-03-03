from app.api.client import async_client
from app.config import settings


async def fetch_quote():
    response = await async_client.get(
        settings.QUOTE_API_URL
    )

    response.raise_for_status()

    data = response.json()

    if not data:
        return "Stay positive.", "Unknown"

    quote_data = data[0]

    return quote_data["q"], quote_data["a"]