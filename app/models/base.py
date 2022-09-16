import datetime
from uuid import uuid1

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


def generate_uuid():
    return str(uuid1())


class BaseModel(Base):
    """Base DB Model."""

    __abstract__ = True

    id = Column(String(36), primary_key=True, default=generate_uuid)
    created = Column(DateTime, default=datetime.datetime.now)
