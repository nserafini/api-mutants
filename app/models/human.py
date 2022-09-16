from sqlalchemy import Column, Text, Boolean

from app.models.base import BaseModel


class HumanModel(BaseModel):
    """Model for Human."""

    __tablename__ = "human"

    dna = Column(Text, nullable=False)
    is_mutant = Column(Boolean, nullable=False)
