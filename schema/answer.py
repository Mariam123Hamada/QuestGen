from pydantic import BaseModel


class AnswerCreate(BaseModel):
    answer: str
    question_id: int


class AnswerResponse(BaseModel):
    id: int
    answer: str
    question_id: int

    model_config = {
        "from_attributes": True
    }