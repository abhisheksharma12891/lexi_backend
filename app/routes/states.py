from fastapi import APIRouter
from app.utils.mappings import get_states

router = APIRouter()

@router.get("/")
def list_states():
    """
    Returns all available states with their internal IDs.
    """
    return get_states()
