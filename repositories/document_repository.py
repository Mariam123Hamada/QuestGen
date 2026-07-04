from sqlalchemy.ext.asyncio import AsyncSession

from models.document import Document
from schema.document import DocumentCreate


class DocumentRepository:

    async def create(
        self,
        db: AsyncSession,
        document: DocumentCreate
    ) -> Document:

        db_document = Document(
            file_name=document.file_name,
            file_type=document.file_type,
            file_size=document.file_size,
            project_id=document.project_id
        )

        db.add(db_document)

        await db.commit()

        await db.refresh(db_document)

        return db_document