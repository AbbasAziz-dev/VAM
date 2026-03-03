import pytest
from unittest.mock import AsyncMock, patch
from pathlib import Path
from app.processors.pdf_processor import PDFProcessor


@pytest.mark.asyncio
async def test_pdf_processor():

    processor = PDFProcessor()

    # Mock extraction
    processor.extract_text = lambda x: "Hello world"

    with patch("app.processors.pdf_processor.detect_language", new=AsyncMock(return_value="en")), \
         patch("app.processors.pdf_processor.fetch_quote", new=AsyncMock(return_value=("Stay strong", "Unknown"))):

        result = await processor.process(Path("dummy.pdf"))

        assert result.filename == "dummy.pdf"
        assert result.word_count == 2
        assert result.language == "en"
        assert result.quote == "Stay strong"
        assert result.author == "Unknown"