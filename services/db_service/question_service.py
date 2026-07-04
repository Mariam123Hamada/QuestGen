from sqlalchemy.ext.asyncio import AsyncSession

from repositories.question_repository import QuestionRepository
from schema.question import QuestionCreate


class QuestionService:
    def __init__(self, question_repository: QuestionRepository):
        self.question_repository = question_repository

    async def create_question(
        self,
        db: AsyncSession,
        question_create: QuestionCreate,
    ):
        return await self.question_repository.create(
            db,
            question_create,
        )