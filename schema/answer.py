from pydantic import BaseModel


class AnswerResponse(BaseModel):
    id: int
    answer: str

    model_config = {
        "from_attributes": True
    }