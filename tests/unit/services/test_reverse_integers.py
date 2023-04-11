from src.api.services.reverse_integers import get_reverse_integers


class TestReverseIntegers:
    async def test_get_reverse_positive_integers_with_zero_digit(
        self,
    ) -> None:
        result = await get_reverse_integers(number=1000)

        assert result == {"reverse_integers": "0001"}

    async def test_get_reverse_negative_integers_with_zero_digit(
        self,
    ) -> None:
        result = await get_reverse_integers(number=-1000)

        assert result == {"reverse_integers": "-0001"}

    async def test_get_reverse_negative_integers(self) -> None:
        result = await get_reverse_integers(number=-123)

        assert result == {"reverse_integers": "-321"}

    async def test_get_reverse_zero_integer(self) -> None:
        result = await get_reverse_integers(number=0)

        assert result == {"reverse_integers": "0"}

    async def test_get_reverse_equal_digits(self) -> None:
        result = await get_reverse_integers(number=666)

        assert result == {"reverse_integers": "666"}
