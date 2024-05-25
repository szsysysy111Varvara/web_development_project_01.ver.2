from pydantic import BaseModel, Field


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=15)
    category_id: int


class QuestionResponse(BaseModel):
    id: int
    text: str
    category_id: int

    class Config:
        from_attributes = True

class CategoryCreateUpdate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str