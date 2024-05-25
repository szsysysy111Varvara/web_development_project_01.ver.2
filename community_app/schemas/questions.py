from pydantic import BaseModel, Field


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=15)


class QuestionResponse(BaseModel):
    id: int
    text: str

    class Config:
        from_attributes = True

class CategoryCreateUpdate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True