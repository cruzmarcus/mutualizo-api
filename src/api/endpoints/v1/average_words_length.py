from fastapi import APIRouter, status

from src.api.services.average_words_length import compute_average_words_length

router = APIRouter()


@router.get("/average-words-length", status_code=status.HTTP_200_OK)
async def average_words_length(phrase: str) -> float:
    """
    For a given phrase, the endpoint must receive a parameter phrase
    and return the average length of the words.
    """
    return await compute_average_words_length(phrase)
