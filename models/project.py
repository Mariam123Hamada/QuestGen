from sqlalchemy.orm import Mapped, mapped_column, relationship 
from sqlalchemy import ForeignKey
from sqlalchemy import String
from db.base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    documents = relationship(
        "Document",
        back_populates="project",
        cascade="all, delete-orphan"
    )