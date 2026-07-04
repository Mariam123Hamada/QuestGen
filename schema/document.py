from pydantic import BaseModel


class DocumentCreate(BaseModel):
    file_name: str
    file_type: str
    file_size: int
    project_id: int


class DocumentResponse(BaseModel):
    id: int
    file_name: str
    file_type: str
    file_size: int
    project_id: int

    model_config = {
        "from_attributes": True
    }