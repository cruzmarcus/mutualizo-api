import re

from src.api.services.tools import utils


async def get_matched_and_mismatched_words(
    sentence_one: str, sentence_two: str
) -> dict[str, list[str]]:
    """
    This endpoint must receive two sentences and return an array
    of words that appear in one sentence and not in the other,
    and an array of common words.
    """
    words_sentence_one = utils.remove_punctuations_marks(sentence_one)
    words_sentence_two = utils.remove_punctuations_marks(sentence_two)

    return {
        "matched_words": sorted(
            list(set(words_sentence_one) & set(words_sentence_two))
        ),
        "mismatched_words": sorted(
            list(set(words_sentence_one) ^ set(words_sentence_two))
        ),
    }
