from abc import ABC, abstractmethod
from pathlib import Path
from app.models import EnrichedDocument


class BaseProcessor(ABC):

    @abstractmethod
    async def process(self, file_path: Path) -> EnrichedDocument:
        pass