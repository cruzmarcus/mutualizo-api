from datetime import datetime, timezone

from fastapi import APIRouter, Depends, status

from src import config
from src.models.api_metadata import ApiMetadata

router = APIRouter()


@router.get(
    '/ping', response_model=ApiMetadata, status_code=status.HTTP_200_OK
)
def ping(
    settings: config.Settings = Depends(config.get_settings),
) -> ApiMetadata:
    """
    Health check endpoint. Returns some API metadata.
    """
    return ApiMetadata(
        name=settings.API_TITTLE,
        version=settings.API_VERSION,
        description=settings.API_DESCRIPTION,
        timestamp=f"{datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec='milliseconds')}Z",
    )
