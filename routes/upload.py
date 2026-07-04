from fastapi import APIRouter, UploadFile, File
from controllers.constarins import ConstraintType , Constraint , UploadResponse


upload_router = APIRouter()

@upload_router.get("/home")
async def home():
    return {"message": "Welcome to the upload route!"}
@upload_router.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    if file.filename.split(".")[-1] not in [constraint.value for constraint in ConstraintType]:
        return UploadResponse(message="File type not supported", status_code=400)
    print("File Size", file.size)
    if file.size < Constraint.MIN_FILE_SIZE or file.size > Constraint.MAX_FILE_SIZE:
        return UploadResponse(message="File size is not within the allowed range", status_code=400)

    return UploadResponse(message="File uploaded successfully", file_name=file.filename, file_type=file.content_type)

