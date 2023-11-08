import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('') / '.env.local'
load_dotenv(dotenv_path=env_path)


class Settings:
    """ App configuration """
    TITLE: str = "Rick and Morty"
    VERSION: str = "0.0.1"
    DEBUG: bool = os.getenv('DEBUG') == 'true'

    # database
    MYSQL_DATABASE_USERNAME: str = os.getenv('MYSQL_DATABASE_USERNAME')
    MYSQL_ROOT_PASSWORD: str = os.getenv('MYSQL_ROOT_PASSWORD')
    MYSQL_DATABASE_HOST: str = os.getenv('MYSQL_DATABASE_HOST')
    MYSQL_DATABASE_PORT: str = os.getenv('MYSQL_DATABASE_PORT')
    MYSQL_DATABASE: str = os.getenv('MYSQL_DATABASE')
    DATABASE_URL: str = (f'mysql+pymysql://'
                         f'{MYSQL_DATABASE_USERNAME}:'
                         f'{MYSQL_ROOT_PASSWORD}@'
                         f'{MYSQL_DATABASE_HOST}:'
                         f'{MYSQL_DATABASE_PORT}/'
                         f'{MYSQL_DATABASE}')


settings = Settings()
