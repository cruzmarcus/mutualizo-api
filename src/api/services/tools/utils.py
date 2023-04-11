import re


def remove_punctuations_marks(sentence: str) -> list[str]:
    """
    This function remove the punctuations marks
    from a string sentence.
    """
    words = sentence.split()
    return [
        re.sub(pattern=r"[^\w\s]", repl="", string=word).lower()
        for word in words
    ]
