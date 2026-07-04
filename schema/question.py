from pydantic import BaseModel


class QuestionCreate(BaseModel):
    question: str
    document_id: int


class QuestionResponse(BaseModel):
    id: int
    question: str
    document_id: int

    model_config = {
        "from_attributes": True
    }