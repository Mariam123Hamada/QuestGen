from sqlalchemy.ext.asyncio import AsyncSession

from repositories.answer_repository import AnswerRepository
from schema.answer import AnswerCreate


class AnswerService:
    def __init__(self, answer_repository: AnswerRepository):
        self.answer_repository = answer_repository

    async def create_answer(
        self,
        db: AsyncSession,
        answer_create: AnswerCreate,
    ):
        return await self.answer_repository.create(
            db,
            answer_create,
        )