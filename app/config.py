from os import getenv
from pydantic import BaseSettings
import os


class BaseConfig(BaseSettings):
    """Class to manage api settings."""

    API_NAME: str = "api-mutants"
    API_VERSION: str = "1.0.0"
    DB_HOST: str = getenv('DB_HOST')
    DB_PORT: int = getenv('DB_PORT')
    DB_NAME: str = getenv('DB_NAME')
    DB_USER: str = getenv('DB_USER')
    DB_PASS: str = getenv('DB_PASS')

    DATABASE_URI: str = f"mysql+mysqldb://{DB_USER}:{DB_PASS}" \
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    DATABASE_CONFIG_DICT: dict = {
        "url": DATABASE_URI,
        "pool_use_lifo": True, 
        "pool_pre_ping": True, 
        "pool_recycle": 3600
    }    

    PATCH_LOGS: str = getenv('PATCH_LOGS', os.path.abspath(os.getcwd()))
    LEVEL_LOGS: str = getenv('LEVEL_LOGS', 'DEBUG')


class TestConfig(BaseConfig):
    """Class to manage tests settings."""

    DATABASE_URI: str = "sqlite:///mutantdb_test.db?check_same_thread=False"
    DATABASE_CONFIG_DICT: dict = {
        "url": DATABASE_URI
    }


settings = BaseConfig()
if getenv('TESTS'):
    settings = TestConfig()
