from fastapi import APIRouter, status

from src.api.services.reverse_integers import get_reverse_integers

router = APIRouter()


@router.get("/reverse-integers", status_code=status.HTTP_200_OK)
async def reverse_integers(number: int) -> str:
    """
    Given an integer, the endpoint must receive an integer as
    a parameter and return the integer with inverted digits.
    Note: The integer can be positive or negative.
    """
    return await get_reverse_integers(number)
