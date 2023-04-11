from src.api.services.average_words_length import compute_average_words_length


class TestReverseIntegers:
    async def test_compute_average_words_length(self) -> None:
        sentence = "Hi all, my name is Tom... I am originally from Brazil."
        result = await compute_average_words_length(sentence)

        assert result == 3.5454545454545454

    async def test_compute_average_words_length_one_word(self) -> None:
        sentence = "Mutualizo!!!"
        result = await compute_average_words_length(sentence)

        assert result == 9
    
    async def test_compute_average_words_length_repetitive_word(self) -> None:
        sentence = "Hello. Hello? Hello! Hello!!!"
        result = await compute_average_words_length(sentence)

        assert result == 5

    async def test_compute_average_words_length_loren_ipsum(self) -> None:
        sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Nullam fermentum finibus justo, ac pellentesque metus tincidunt a. "
        "Quisque vel arcu id lacus euismod malesuada. Vestibulum sed feugiat "
        "mauris, sed pellentesque diam. Quisque vitae lacus sed nunc auctor "
        "sodales. Ut bibendum luctus pellentesque. Donec facilisis nulla "
        "fermentum enim rutrum pellentesque. Nullam varius posuere dolor, "
        "et aliquam orci tincidunt a. Pellentesque habitant morbi tristique "
        "senectus et netus et malesuada fames ac turpis egestas. "
        "Aenean porttitor scelerisque sapien, blandit vulputate nulla laoreet ac. "
        " Nunc venenatis vestibulum augue, sit amet pellentesque risus efficitur ut. "
        "Aenean eu elit luctus, cursus elit ut, tincidunt ligula. Etiam "
        "interdum lorem vel urna blandit lobortis."

        result = await compute_average_words_length(sentence)

        assert result == 5.875
