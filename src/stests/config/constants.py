"""Module for configs test framework."""
import os
from enum import Enum


class ConstantPaths:
    """Class contains paths."""

    PATH_TEST_DATA = 'test_data/test_data.yml'


class APIRoutes(str, Enum):
    """Class contains endpoints."""

    CARDS = '/get_cards'
    DETAIL_CARD = '/card_detail_view'
    RUN_PIPELINE = '/run_pipeline'

    def __str__(self) -> str:
        """Return value."""
        return self.value


class APITokens(str, Enum):
    """Class contains test key for different roles."""

    DATA_ENGINEER = os.getenv('DATA_ENGINEER')
    PROJECT_MANAGER = os.getenv('PROJECT_MANAGER')
    SITE_IM_PERSON = os.getenv('SITE_IM_PERSON')
    NOT_VALID_TOKEN = 'token'

    def __str__(self) -> str:
        """Return value."""
        return self.value


class APIUrls(str, Enum):
    """Class contains paths."""

    DEV_URL = 'https://dummyapi.io/data/v1'
    STAGE_URL = ''
    PROD_URL = ''

    def __str__(self) -> str:
        """Return value."""
        return self.value


class Environment(str, Enum):
    """Class contains environments."""

    DEV_ENV = True
    STAGE_ENV = False or os.getenv('test')
