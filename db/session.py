from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy.orm import async_sessionmaker
from db.database import engine


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session