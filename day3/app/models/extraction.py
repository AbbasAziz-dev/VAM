from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional
from datetime import datetime


class ExtractionResult(BaseModel):
    doc_id: str
    entities: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    metadata: Dict[str, str] = {}
    confidence_score: float = Field(ge=0.0, le=1.0)
    processed_at: datetime = Field(default_factory=datetime.utcnow)

    @field_validator("confidence_score")
    @classmethod
    def validate_confidence(cls, value: float):
        if value < 0.3:
            raise ValueError("confidence_score too low")
        return value