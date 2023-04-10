from fastapi import APIRouter

from src.api.endpoints.v1 import average_words_length, ping, reverse_integers

api_router = APIRouter()

api_router.include_router(ping.router, tags=["Ping"], prefix="/v1")


api_router.include_router(
    reverse_integers.router,
    tags=["Reverse Integers"],
    prefix="/v1",
)

api_router.include_router(
    average_words_length.router,
    tags=["Average Words Length"],
    prefix="/v1",
)
