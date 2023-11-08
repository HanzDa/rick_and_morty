from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.database.base import Base


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    url = Column(String(500), nullable=True, unique=True)
