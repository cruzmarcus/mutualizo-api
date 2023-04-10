import json

from pydantic import BaseModel

PING_SCHEMA_RESPONSE: dict = json.load(
    open("src/api/swagger_schemas/response_body/ping-schema.json")
)


class ApiMetadata(BaseModel):
    """
    Basic API metadata to return to ping request.
    """

    name: str
    version: str
    description: str
    timestamp: str

    class Config:
        schema_path = {'example': PING_SCHEMA_RESPONSE}
