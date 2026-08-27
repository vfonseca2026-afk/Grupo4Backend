from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

NO_HTML_PATTERN = r"^[^<>]*$"


class Pet(BaseModel):
    id: str
    studentId: str
    name: str
    species: str
    age: int | None = None
    createdAt: datetime
    updatedAt: datetime


class CreatePetDto(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1, max_length=50, pattern=NO_HTML_PATTERN)
    species: str = Field(min_length=1, max_length=50, pattern=NO_HTML_PATTERN)
    age: int | None = Field(default=None, ge=0, le=100)


class UpdatePetDto(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str | None = Field(
        default=None, min_length=1, max_length=50, pattern=NO_HTML_PATTERN
    )

    species: str | None = Field(
        default=None, min_length=1, max_length=50, pattern=NO_HTML_PATTERN
    )

    age: int | None = Field(default=None, ge=0, le=100)
