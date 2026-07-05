from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, UploadFile, File , Depends
from db.session import get_db
from dependencies.services import(
    get_project_service ,
    get_document_service ,
    get_question_service ,
    get_answer_service
    )
from services.db_service.project_service import ProjectService
from services.db_service.document_service import DocumentService
from services.db_service.question_service import QuestionService
from services.db_service.answer_service import AnswerService

from controllers.constarins import ConstraintType , Constraint , UploadResponse
from services.api_service.upload_service import UploadService 

def get_upload_service(
    db: AsyncSession = Depends(get_db),
    project_service: ProjectService = Depends(get_project_service),
    document_service: DocumentService = Depends(get_document_service),
    question_service: QuestionService = Depends(get_question_service),
    answer_service: AnswerService = Depends(get_answer_service),
):
    return UploadService(
        db=db,
        project_service=project_service,
        document_service=document_service,
        question_service=question_service,
        answer_service=answer_service,
    )
upload_router = APIRouter()

@upload_router.get("/home")
async def home():
    return {"message": "Welcome to the upload route!"}

# @upload_router.post("/upload", response_model=UploadResponse)
# async def upload_file(file: UploadFile = File(...)):
#     if file.filename.split(".")[-1] not in [constraint.value for constraint in ConstraintType]:
#         return UploadResponse(message="File type not supported", status_code=400)
#     print("File Size", file.size)
#     if file.size < Constraint.MIN_FILE_SIZE or file.size > Constraint.MAX_FILE_SIZE:
#         return UploadResponse(message="File size is not within the allowed range", status_code=400)

#     return UploadResponse(message="File uploaded successfully", file_name=file.filename, file_type=file.content_type)

@upload_router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    upload_service: UploadService = Depends(get_upload_service),
):
    print("UploadService is running")
    return await upload_service.upload_file(file)