from sqlalchemy.ext.asyncio import AsyncSession


from repositories.document_repository import DocumentRepository
from schema.document import DocumentCreate 

class DocumentService:
    def __init__(self , document_repository: DocumentRepository):
        self.document_repository = document_repository
    
    async def create_document(self , db: AsyncSession , document_create: DocumentCreate):
        return await self.document_repository.create(db , document_create)