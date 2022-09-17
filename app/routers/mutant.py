from fastapi import APIRouter, HTTPException

from app.schemas.mutant import MutantCheckRequestSchema
from app.services.human import HumanService

mutant_router = APIRouter()


@mutant_router.post("", response_model=bool)
def check(payload: MutantCheckRequestSchema):
    """Check DNA Mutant."""

    dna = payload.dict().get('dna')
    human = HumanService(dna).save()
    if not human.is_mutant:
        raise HTTPException(status_code=403)
    return human.is_mutant
