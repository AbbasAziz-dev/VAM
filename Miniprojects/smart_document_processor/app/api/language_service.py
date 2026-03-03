from app.api.client import async_client
from app.config import settings


async def detect_language(text: str) -> str:
    headers = {
        "Authorization": f"Bearer {settings.LANGUAGE_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {"q": text}

    response = await async_client.post(
        settings.LANGUAGE_API_URL,
        json=payload,
        headers=headers
    )

    response.raise_for_status()
    data = response.json()

    # Case 1: API returns list
    if isinstance(data, list):
        if len(data) > 0:
            return data[0].get("language", "unknown")
        return "unknown"

    # Case 2: API returns dict with nested structure
    