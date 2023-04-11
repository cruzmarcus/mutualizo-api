import re


async def get_average_words_length(sentence: str) -> float:
    words = sentence.split()
    words = [
        re.sub(pattern=r"[^\w\s]", repl="", string=word) for word in words
    ]
    return sum(len(word) for word in words) / float(len(words))
