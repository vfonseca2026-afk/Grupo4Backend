from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

NO_HTML_PATTERN = r"^[^<>]*$"


class Student(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int
    createdAt: datetime
    updatedAt: datetime


class CreateStudentDto(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=3, max_length=100, pattern=NO_HTML_PATTERN)
    email: EmailStr
    age: int = Field(ge=18, le=99)


class UpdateStudentDto(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str | None = Field(
        default=None, min_length=3, max_length=100, pattern=NO_HTML_PATTERN
    )
    email: EmailStr | None = None
    age: int | None = Field(default=None, ge=18, le=99)
