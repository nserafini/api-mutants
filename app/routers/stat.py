from fastapi import APIRouter

from app.schemas.stat import StatResponseSchema
from app.services.stat import StatService

stat_router = APIRouter()


@stat_router.get("", response_model=StatResponseSchema)
def get_stats():
    """Retrieves Mutant Stats."""

    return StatService.get_stats()
