from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)

    question: Mapped[str] = mapped_column(Text)

    difficulty: Mapped[str] = mapped_column(String(20))

    question_type: Mapped[str] = mapped_column(String(30))

    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id")
    )

    document = relationship(
        "Document",
        back_populates="questions"
    )

    answer = relationship(
        "Answer",
        back_populates="question",
        uselist=False,
        cascade="all, delete-orphan"
    )