from pydantic import BaseModel, Field, model_validator


class ProcessingConfig(BaseModel):
    language: str = Field(default="en")
    extract_entities: bool = True
    extract_keywords: bool = True
    max_keywords: int = Field(default=10, ge=1, le=50)

    @model_validator(mode="after")
    def validate_config(self):
        if not self.extract_entities and not self.extract_keywords:
            raise ValueError(
                "At least one extraction option must be enabled"
            )
        return self