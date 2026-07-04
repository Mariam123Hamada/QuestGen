from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from sqlalchemy import ForeignKey

from db.base import Base


class Answer(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True)

    answer: Mapped[str] = mapped_column(Text)

    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id"),
        unique=True
    )

    question = relationship(
        "Question",
        back_populates="answer"
    )