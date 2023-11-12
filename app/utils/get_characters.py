import json
import httpx
import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import HTTPException

env_path = Path('') / '.env.local'
load_dotenv(env_path)


async def get_characters(**kwargs):
    """
        Asynchronously gets characters from a service.

        :return: A list of character results from the service.
        :raises HTTPException: If there was an error getting characters from the service.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(os.getenv('SERVICE_URL'), params=kwargs)

        if response.status_code != 200:
            raise HTTPException(
                detail="Failed to get characters from external service",
                status_code=response.status_code
            )
    data = json.loads(response.content)

    return data.get('results', [])
