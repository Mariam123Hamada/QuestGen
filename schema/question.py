from pydantic import BaseModel
from typing import List


class QuestionCreate(BaseModel):
    question: str
    difficulty: str
    question_type: str
    document_id: int
    choices: List[str]



class QuestionResponse(BaseModel):
    id: int
    question: str
    difficulty: str
    question_type: str
    document_id: int
    choices: List[str]

    model_config = {
        "from_attributes": True
    }