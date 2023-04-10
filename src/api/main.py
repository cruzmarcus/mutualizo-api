from fastapi import FastAPI

from src import config
from src.api.endpoints.router import api_router

settings = config.get_settings()

app = FastAPI(
    title=settings.API_TITTLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
)


app.include_router(api_router)
