from pydantic import BaseModel


class ApiMetadata(BaseModel):
    """
    Basic API metadata to return to ping request.
    """

    name: str
    version: str
    description: str
    timestamp: str

    class Config:
        schema_path = {
            "example": {
                "name": "Mutualizo API",
                "version": "1.0.0",
                "description": "Mutualizo Test API",
                "datetime": "2023-04-10T23:33:00.666Z",
            }
        }


class ReverseIntegersResponse(BaseModel):
    reverse_integers: str

    class Config:
        schema_path = {"example": {"reverse_integers": "-321"}}


class AverageWordsLengthResponse(BaseModel):
    average_words_length: float

    class Config:
        schema_path = {"example": {"average_words_length": 5.0}}


class MatchedAndMismatchedWordsResponse(BaseModel):
    matched_words: list[str]
    mismatched_words: list[str]

    class Config:
        schema_path = {
            "example": {
                "matched_words": ["city", "really"],
                "mismatched_words": [
                    "a",
                    "are",
                    "by",
                    "heavy",
                    "hit",
                    "in",
                    "meet",
                    "our",
                    "pleased",
                    "storm",
                    "the",
                    "to",
                    "was",
                    "we",
                    "you",
                ],
            }
        }
