import re

from src.api.services.tools import utils


async def get_average_words_length(sentence: str) -> float:
    """
    Service layer for the endpoint /average-words-length.
    The function processes the average value of the words length.
    """

    words = utils.remove_punctuations_marks(sentence)

    return sum(len(word) for word in words) / float(len(words))
