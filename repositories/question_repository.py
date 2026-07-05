from sqlalchemy.ext.asyncio import AsyncSession

from models.question import Question
from schema.question import QuestionCreate


class QuestionRepository:

    async def create(
        self,
        db: AsyncSession,
        question: QuestionCreate,
    ) -> Question:

        db_question = Question(
            question=question.question,
            difficulty=question.difficulty,
            question_type=question.question_type,
            choices=question.choices,
            document_id=question.document_id,
        )

        db.add(db_question)

        await db.commit()

        await db.refresh(db_question)

        return db_question