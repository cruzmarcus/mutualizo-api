from src.api.services.average_words_length import compute_average_words_length


class TestReverseIntegers:
    async def test_compute_average_words_length(self) -> None:
        sentence = "Hi all, my name is Tom... I am originally from Brazil."
        result = await compute_average_words_length(sentence)

        assert result == 3.9
    
