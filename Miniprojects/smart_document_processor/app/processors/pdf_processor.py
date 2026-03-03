import asyncio
from pathlib import Path
from PyPDF2 import PdfReader
from app.processors.base import BaseProcessor
from app.models import EnrichedDocument
from app.api.language_service import detect_language
from app.api.quote_service import fetch_quote


class PDFProcessor(BaseProcessor):

    def extract_text(self, file_path: Path) -> str:
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        return text

    async def process(self, file_path: Path) -> EnrichedDocument:
        text = self.extract_text(file_path)

        # Safety check
        if not text.strip():
            text = "Empty document"

        language_task = asyncio.create_task(detect_language(text))
        quote_task = asyncio.create_task(fetch_quote())

        language, (quote, author) = await asyncio.gather(
            language_task,
            quote_task
        )

        return EnrichedDocument(
            filename=file_path.name,
            word_count=len(text.split()),
            language=language,
            quote=quote,
            author=author
        )