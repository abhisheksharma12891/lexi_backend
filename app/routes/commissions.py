from fastapi import APIRouter
from app.utils.mappings import get_commissions

router = APIRouter()

@router.get("/{state_id}")
def list_commissions(state_id: int):
    """
    Returns all commissions for a given state ID.
    """
    return get_commissions(state_id)
