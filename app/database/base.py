from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.characters import Character
from app.models.locations import Location
