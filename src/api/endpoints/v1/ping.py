from datetime import datetime, timezone

from fastapi import APIRouter, Depends, status

from src import config
from src.api import models

router = APIRouter()


@router.get("/ping", status_code=status.HTTP_200_OK)
def ping(
    settings: config.Settings = Depends(config.get_settings),
) -> models.ApiMetadata:
    """
    Health check endpoint. Returns some API metadata.
    """
    return models.ApiMetadata(
        name=settings.API_TITTLE,
        version=settings.API_VERSION,
        description=settings.API_DESCRIPTION,
        timestamp=f"{datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec='milliseconds')}Z",
    )
