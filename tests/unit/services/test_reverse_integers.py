from src.api.services.reverse_integers import get_reverse_integers


class TestReverseIntegers:
    async def test_compute_reverse_positive_integers_with_zero_digit(
        self,
    ) -> None:
        result = await get_reverse_integers(number=1000)

        assert result == "0001"

    async def test_compute_reverse_negative_integers_with_zero_digit(
        self,
    ) -> None:
        result = await get_reverse_integers(number=-1000)

        assert result == "-0001"

    async def test_compute_reverse_negative_integers(self) -> None:
        result = await get_reverse_integers(number=-123)

        assert result == "-321"

    async def test_compute_reverse_zero_integer(self) -> None:
        result = await get_reverse_integers(number=0)

        assert result == "0"
