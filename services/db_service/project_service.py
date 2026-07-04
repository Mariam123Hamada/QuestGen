from sqlalchemy.ext.asyncio import AsyncSession

from repositories.project_repository import ProjectRepository
from schema.project import ProjectCreate

class ProjectService:
    def __init__(self , project_repository: ProjectRepository):
        self.project_repository = project_repository
    
    async def create_project(self , db: AsyncSession , project_create: ProjectCreate):
        return await self.project_repository.create(db , project_create)