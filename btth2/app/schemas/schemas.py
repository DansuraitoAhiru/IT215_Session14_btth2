from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    full_name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    major: str = Field(min_length=1)
    gpa: float = Field(ge=1, le=10)

class StudentUpdate(BaseModel):
    full_name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    major: str = Field(min_length=1)
    gpa: float = Field(ge=1, le=10)