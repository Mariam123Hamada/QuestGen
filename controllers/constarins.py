from enum import Enum 
from pydantic import BaseModel

class ConstraintType(Enum):
    """ This is the File Type Suporrted on that Project """
    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"
    
class Constraint:
    MIN_FILE_SIZE = 1 * 1024  # 1 KB    
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
    


class UploadResponse(BaseModel):
    message: str
    status_code: int = 200
    file_name: str = None
    file_type: str = None
    
    
        
    
    