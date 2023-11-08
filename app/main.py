from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.config import settings
from app.database.base import Base
from app.database.session import engine

from app.routes import characters


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.TITLE,
    debug=settings.DEBUG,
    version=settings.VERSION,
    lifespan=lifespan
)

app.include_router(characters.router, prefix='/api')
 