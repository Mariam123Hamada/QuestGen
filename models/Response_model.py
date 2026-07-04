from pydantic import BaseModel

class UploadResponse(BaseModel):
    message: str
    status_code: int = 200
    file_name: str = None
    file_type: str = None
    
    
    