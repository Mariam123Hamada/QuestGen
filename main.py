from fastapi import FastAPI , Depends
from routes.upload import upload_router
from utils.helper import lifespan
from db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession


app = FastAPI(lifespan=lifespan)
app.include_router(upload_router)

@app.get("/")
async def read_root(db: AsyncSession = Depends(get_db)):
    return {"Hello": " Hello World From the main  route "}

