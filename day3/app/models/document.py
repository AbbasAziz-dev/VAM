from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class DocumentInput(BaseModel):
    doc_id: str = Field(..., description="Unique document identifier")
    text: str = Field(..., min_length=10)
    source: str = Field(..., description="Document source")
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)

    @field_validator("doc_id")
    @classmethod
    def validate_doc_id(cls, value: str):
        if not value.strip():
            raise ValueError("doc_id cannot be empty")
        return value

    @field_validator("source")
    @classmethod
    def validate_source(cls, value: str):
        allowed_sources = {"pdf", "email", "web"}
        if value.lower() not in allowed_sources:
            raise ValueError(f"source must be one of {allowed_sources}")
        return value.lower()