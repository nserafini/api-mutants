from app.schemas.base import BaseSchema


class MutantCheckRequestSchema(BaseSchema):
    """Schema for Mutant Check Request."""

    dna: list


class MutantStatsResponseSchema(BaseSchema):
    """Schema for Mutant Stats Response."""

    count_mutant_dna: int
    count_human_dna: int
    ratio: float
