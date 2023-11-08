from sqlalchemy.orm import Session

from app.models.characters import Character
from app.models.locations import Location


def create_location(location_json, db):
    """
        The create_location function takes in a JSON object and adds it to the database.

        :param location_json: Pass in the json data that is used to create a new location
        :param db: database session
        :return: The location object that was created
    """
    location = Location(**location_json)
    db.add(location)
    db.commit()
    db.refresh(location)

    return location


def get_location(location_json, db: Session):
    """
        The get_location function takes a location_json object as an argument and returns the location
        object from the database. If no such object exists, it creates one.

        :param location_json: Get the location data from the json file.
        :param db: database session.
        :return: A location object
    """
    location = db.query(Location).filter_by(url=location_json.get('url')).first()

    if not location:
        location = create_location(location_json, db)

    return location


def get_new_characters(all_characters, db: Session):
    """
        The get_new_characters function takes in a list of all characters and returns a list of new characters.
        It does this by comparing the names of the existing characters to those in the database, and returning
        only those that are not already present.

        :param all_characters: Check if the character already exists in the database.
        :param db: database session.
        :return: All the characters that are not in the all_characters list.
    """
    existing_names = {char.get('name') for char in all_characters if char.get('name')}
    existing_characters = db.query(Character).filter(Character.name.in_(existing_names)).all()
    existing_names = {char.name for char in existing_characters}

    new_characters = [char for char in all_characters if char.get('name') not in existing_names]
    return new_characters


def add_locations(character, db: Session):

    """
        The add_locations function takes a character dictionary as an argument and adds
        the location_id and origin_id keys to it. The values of these keys are the ids of the locations
        in our database that correspond to those listed in the character's 'location'
        and 'origin' fields. If no such location exists, we create one.

        :param character: Pass in the character dictionary.
        :param db: database session.
        :return: The character with the origin and location ids added.
    """
    origin = character.get('origin')
    location = character.get('location')

    if origin:
        origin = get_location(origin, db)
        character['origin_id'] = origin.id
    if location:
        location = get_location(location, db)
        character['location_id'] = location.id


def bulk_create_characters(characters_json_list, db: Session):
    """
        The bulk_create_characters function takes a list of character dictionaries and creates them in the database.
        It first checks if the characters already exist, and only adds new ones to the database. It also creates any
        locations that are not yet in the database.

        :param characters_json_list: Pass in a list of character dictionaries
        :param db: database session.
        :return: The amount of characters created
    """
    characters_json_list = get_new_characters(characters_json_list, db)
    characters = []
    amount = 0
    for c in characters_json_list:
        add_locations(c, db)

        c.pop('id')
        character = Character(**c)
        characters.append(character)
        amount += 1

    db.bulk_save_objects(characters)
    db.commit()
    return amount
