async def get_reverse_integers(number: int) -> dict[str, str]:
    """
    Service layer for the endpoint /reverse-integers.
    The function can process number negative, positive or zero.
    """
    reverted_number = list(reversed(str(number)))

    reverse_integers = (
        "".join(reverted_number)
        if "-" not in reverted_number[-1]
        else f"-{''.join(reverted_number[:-1])}"
    )

    return {"reverse_integers": reverse_integers}
