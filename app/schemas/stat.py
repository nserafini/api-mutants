from app.schemas.base import BaseSchema


class StatResponseSchema(BaseSchema):
    """Schema for Stat Response."""

    count_mutant_dna: int
    count_human_dna: int
    ratio: float
