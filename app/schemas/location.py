from pydantic import BaseModel, Field


class Location(BaseModel):
    name: str = Field(default='Earth', max_length=100)
    url: str = Field(default='www.example_url.com', max_length=500)
