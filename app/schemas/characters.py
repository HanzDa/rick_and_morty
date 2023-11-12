from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

from app.schemas.location import Location


class Status(Enum):
    """ Possible status of a character """

    ALIVE = "Alive"
    DEAD = "Dead"
    UNKNOWN = "unknown"


class Gender(Enum):
    """ All gender known in Rick and Morty series """

    FEMALE = "Female"
    MALE = "Male"
    GENDERLESS = "Genderless"
    UNKNOWN = "unknown"


class Character(BaseModel):
    """ Representation of a character in the Rick and Morty series """
    name: str = Field(default="Rick Sanchez", max_length=255)
    status: Status = Field(default=Status.ALIVE)
    species: str = Field(default="Human", max_length=100)
    type: str = Field(default="", max_length=255)
    gender: Gender = Field(default=Gender.MALE)
    image: str = Field(default="www.example_image_url.com", max_length=500)
    url: str = Field(default="www.example_url.com", max_length=500)
    episode: list[str]
    origin: Location
    location: Location
    created: datetime
