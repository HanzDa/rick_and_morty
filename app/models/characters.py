from sqlalchemy import Column, String, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.database.base import Base


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    status = Column(String(50), default='', nullable=True)
    species = Column(String(100), default='', nullable=True)
    type = Column(String(255), default='', nullable=True)
    gender = Column(String(50), default='', nullable=True)
    image = Column(String(500), default='', nullable=True, unique=True)
    url = Column(String(500), default='', nullable=True)
    episode = Column(JSON(none_as_null=True), default=[])
    created = Column(String(100), nullable=True)

    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship("Location", foreign_keys=[location_id])
    origin_id = Column(Integer, ForeignKey('locations.id'))
    origin = relationship("Location", foreign_keys=[origin_id])
