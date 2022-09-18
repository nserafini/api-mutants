from sqlalchemy import Column, Boolean
from sqlalchemy.sql.sqltypes import JSON
from app.models.base import BaseModel


class HumanModel(BaseModel):
    """Model for Human."""

    __tablename__ = "human"

    dna = Column(JSON, nullable=False)
    is_mutant = Column(Boolean, nullable=False)
