"""Module for configs test framework."""
import os
from enum import Enum


class ConstantPaths:
    """Class contains paths."""

    PATH_TEST_DATA = 'test_data/test_data.yml'


class APIRoutes(str, Enum):
    """Class contains endpoints."""

    CARDS = '/cards_information'
    DETAIL_CARD = '/card_detail_view'
    RUN_PIPELINE = '/run_pipeline'

    def __str__(self) -> str:
        """Return value."""
        return self.value


class APITokens(str, Enum):
    """Class contains test key for different roles."""

    DATA_ENGINEER_TOKEN = os.getenv('DATA_ENGINEER_TOKEN')
    PROJECT_MANAGER_TOKEN = os.getenv('PROJECT_MANAGER_TOKEN')
    SITE_IM_PERSON_TOKEN = os.getenv('SITE_IM_PERSON_TOKEN')
    NOT_VALID_TOKEN = 'token'
    EMPTY_TOKEN = ''

    def __str__(self) -> str:
        """Return value."""
        return self.value


class APIUrls(str, Enum):
    """Class contains paths."""

    DEV_URL = 'https://localhost:9090'
    STAGE_URL = ''
    PROD_URL = ''

    def __str__(self) -> str:
        """Return value."""
        return self.value


class Environment(str, Enum):
    """Class contains environments."""

    DEV_ENV = False or os.getenv('DEV_ENV')
    STAGE_ENV = False or os.getenv('STAGE_ENV')
