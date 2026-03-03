import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from app.api.language_service import detect_language
from app.api.quote_service import fetch_quote


@pytest.mark.asyncio
async def test_detect_language_success():

    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"language": "en"}
    ]
    mock_response.raise_for_status.return_value = None

    async_mock_post = AsyncMock(return_value=mock_response)

    with patch("app.api.language_service.async_client.post", async_mock_post):
        result = await detect_language("Hello world")
        assert result == "en"


@pytest.mark.asyncio
async def test_fetch_quote_success():

    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"q": "Stay strong", "a": "Unknown"}
    ]
    mock_response.raise_for_status.return_value = None

    async_mock_get = AsyncMock(return_value=mock_response)

    with patch("app.api.quote_service.async_client.get", async_mock_get):
        quote, author = await fetch_quote()

        assert quote == "Stay strong"
        assert author == "Unknown"