import asyncio

import httpx
import pytest

from src import config
from src.api.main import app


@pytest.fixture
def settings():
    return config.get_settings()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def client(settings):
    async with httpx.AsyncClient(
        app=app, base_url=f"http://{settings.API_ADDRESS}"
    ) as client:
        yield client
