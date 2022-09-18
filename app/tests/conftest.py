import pytest
from sqlalchemy import create_engine

from app.config import settings
from app.models.base import BaseModel


@pytest.fixture(scope="function", autouse=True)
def renew_db():
    engine = create_engine(settings.DATABASE_URI)
    BaseModel.metadata.create_all(engine)
    yield engine
    BaseModel.metadata.drop_all(engine)
