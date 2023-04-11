from src.api.services.matched_and_mismatched_words import (
    get_matched_and_mismatched_words,
)


class TestMatchedAndMisMatchedWords:
    async def test_get_matched_and_mismatched_words(self) -> None:
        sentence_one = "We are really pleased to meet you in our city"
        sentence_two = "The city was hit by a really heavy storm"

        result = await get_matched_and_mismatched_words(
            sentence_one, sentence_two
        )

        assert result == {
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

    async def test_get_matched_and_mismatched_words_similar_sentences(
        self,
    ) -> None:
        sentence_one = "To be or not to be. That is the question!"
        sentence_two = "To be or not to be. That is the question!"

        result = await get_matched_and_mismatched_words(
            sentence_one, sentence_two
        )

        assert result == {
            "matched_words": [
                "be",
                "is",
                "not",
                "or",
                "question",
                "that",
                "the",
                "to",
            ],
            "mismatched_words": [],
        }
