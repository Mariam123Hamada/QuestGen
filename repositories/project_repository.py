from sqlalchemy.ext.asyncio import AsyncSession

from models.project import Project
from schemas.project import ProjectCreate


class ProjectRepository:

    async def create(
        self,
        db: AsyncSession,
        project: ProjectCreate
    ) -> Project:

        db_project = Project(
            name=project.name
        )

        db.add(db_project)

        await db.commit()

        await db.refresh(db_project)

        return db_project