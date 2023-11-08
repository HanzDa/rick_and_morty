from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.characters import Character
from app.models.characters import Character as DbCharacter
from app.utils.get_characters import get_characters
from app.database.crud import bulk_create_characters

router = APIRouter(tags=['characters'])


@router.get('/characters', response_model=list[Character])
async def get_characters_from_service(page=1):

    """
        The get_characters_from_service function is a coroutine that gets characters from the Rick and Morty API.
        It takes in an optional page parameter, which defaults to 1 if not provided.

        :param page: Specify the page number of the api that we want to get data from
        :return: A list of characters
    """
    characters = await get_characters(page=page)
    return characters


@router.get('/characters/{character_id}', response_model=Character)
def get_character(character_id: int, db: Session = Depends(get_db)):
    """
        The get_character function will return a character object from the database.

        :param character_id: int: Specify the character id that is passed in as a path parameter
        :param db: Session: Session of the database
        :return: The character object getting from the database
    """
    character = db.query(DbCharacter).filter_by(id=character_id).first()

    if character is None:
        raise HTTPException(
            detail=f"Character with id {character_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return character


@router.post('/characters')
async def create_character(page=1, db: Session = Depends(get_db)) -> JSONResponse:
    """
        The create_character function creates a new characters in the database
        getting data from external service (Rick and morty API).

        :param page: Determine which page of results to retrieve from external api
        :return: A JSONResponse with a status code of 201 if successful
    """
    characters = await get_characters(page=page)

    amount = bulk_create_characters(characters, db)

    return JSONResponse(
        content=f'{amount} new characters were created',
        status_code=status.HTTP_201_CREATED
    )
