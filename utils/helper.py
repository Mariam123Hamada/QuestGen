from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.database import engine
from db.base import Base

# Import all models
from models.project import Project
from models.document import Document
from models.question import Question
from models.answer import Answer


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield