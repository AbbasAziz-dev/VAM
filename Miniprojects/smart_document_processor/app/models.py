from pydantic import BaseModel, Field
from pathlib import Path
from datetime import datetime


class DocumentInput(BaseModel):
    file_path: Path

    @property
    def filename(self) -> str:
        return self.file_path.name


class EnrichedDocument(BaseModel):
    filename: str
    word_count: int
    language: str
    quote: str
    author: str
    