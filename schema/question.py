from pydantic import BaseModel


class QuestionResponse(BaseModel):
    id: int
    question: str
    difficulty: str
    question_type: str

    model_config = {
        "from_attributes": True
    }