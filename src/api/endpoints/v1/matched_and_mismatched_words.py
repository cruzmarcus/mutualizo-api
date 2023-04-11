from fastapi import APIRouter, status

from src.api import models
from src.api.services.matched_and_mismatched_words import (
    get_matched_and_mismatched_words,
)

router = APIRouter()


@router.get("/matched-and-mismatched-words", status_code=status.HTTP_200_OK)
async def matched_and_mismatched_words(
    sentence_one: str, sentence_two: str
) -> models.MatchedAndMismatchedWordsResponse:
    """
    This endpoint must receive two sentences and return an array
    of words that appear in one sentence and not in the other,
    and an array of common words.
    """
    return await get_matched_and_mismatched_words(sentence_one, sentence_two)
