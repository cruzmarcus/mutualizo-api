import re

PUNCTUATION_MARKS: str = '".,;:!?-()'


async def compute_average_words_length_original(sentence: str) -> float:
    """
    Service layer for the endpoint /average-words-length.
    The function processes a
    """
    filtered_sentence = "".join(
        filter(lambda character: character not in PUNCTUATION_MARKS, sentence)
    )

    words = [word for word in filtered_sentence.split() if word]

    return sum(len(word) for word in words) / len(words)


async def compute_average_words_length(sentence: str) -> float:
    words = sentence.split()
    words = [
        re.sub(pattern=r"[^\w\s]", repl="", string=word) for word in words
    ]
    return sum(len(word) for word in words) / float(len(words))
