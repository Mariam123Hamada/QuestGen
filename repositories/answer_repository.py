from sqlalchemy.ext.asyncio import AsyncSession

from models.answer import Answer
from schema.answer import AnswerCreate


class AnswerRepository:

    async def create(
        self,
        db: AsyncSession,
        answer: AnswerCreate,
    ) -> Answer:

        db_answer = Answer(
            answer=answer.answer,
            question_id=answer.question_id,
        )

        db.add(db_answer)

        await db.commit()

        await db.refresh(db_answer)

        return db_answer