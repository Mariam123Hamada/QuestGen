from fastapi import APIRouter, UploadFile, File
from controllers.constarins import ConstraintType
from models.Response_model import UploadResponse

upload_router = APIRouter()

@upload_router.get("/home")
def home():
    return {"message": "Welcome to the upload route!"}
@upload_router.post("/upload", response_model=UploadResponse)
def upload_file(file:UploadFile = File(...)):
    if file.filename.split(".")[-1] not in [constraint.value for constraint in ConstraintType]:
        return UploadResponse(message="File type not supported", status_code=400)
    return UploadResponse(message="File uploaded successfully", file_name=file.filename, file_type=file.content_type)