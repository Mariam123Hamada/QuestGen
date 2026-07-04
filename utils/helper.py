from pydantic import BaseModel

class EnvData(BaseModel):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

env_data = EnvData()