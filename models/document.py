from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String , Integer , FoereignKey
from db.base import Base

class Document(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(primary_key=True)

    file_name: Mapped[str] = mapped_column(String(255))
    file_type: Mapped[str] = mapped_column(String(50))
    file_size: Mapped[int] = mapped_column(Integer)
    
    project_id: Mapped[int] = mapped_column(
        FoereignKey("projects.id")
    )
    project = relationship("Project", back_populates="documents")
    questions = relationship(
        "Question" , 
        back_populates="document" ,
        cascade="all, delete-orphan"
    )