import json
import httpx
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('') / '.env.local'
load_dotenv(env_path)


async def get_characters(**kwargs):
    """
    The get_characters function returns a list of characters from the Rick and morty API.

    :return: A list of dictionaries
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(os.getenv('SERVICE_URL'), params=kwargs)
    data = json.loads(response.content)

    return data.get('results', [])
