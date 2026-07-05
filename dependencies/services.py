from services.db_service.project_service import ProjectService
from services.db_service.document_service import DocumentService
from services.db_service.question_service import QuestionService
from services.db_service.answer_service import AnswerService

from repositories.project_repository import ProjectRepository
from repositories.document_repository import DocumentRepository
from repositories.question_repository import QuestionRepository
from repositories.answer_repository import AnswerRepository


def get_project_service() -> ProjectService:
    return ProjectService(ProjectRepository())


def get_document_service() -> DocumentService:
    return DocumentService(DocumentRepository())


def get_question_service() -> QuestionService:
    return QuestionService(QuestionRepository())


def get_answer_service() -> AnswerService:
    return AnswerService(AnswerRepository())