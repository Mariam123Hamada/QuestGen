from enum import Enum 

class ConstraintType(Enum):
    """ This is the File Type Suporrted on that Project """
    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"
    
class Constraint:
    MIN_FILE_SIZE = 1 * 1024  # 1 KB    
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
    
    