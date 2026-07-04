from sqlalchemy.ext.asyncio import create_async_engine
from utils.helper import env_data


engine = create_async_engine(
    env_data.DATABASE_URL,
    echo=True,
    future=True,
)