"""Collect all fixtures."""
import pytest
from stests.config.constants import APITokens
from stests.config.constants import APIUrls
from stests.config.constants import Environment
from stests.lib.api.api_client import APIClient

from src.stests.config.constants import ConstantPaths
from src.stests.utils.utils import read_yaml_file


@pytest.fixture(scope='session')
def api_url() -> str:
    """Return the appropriate API URL based on the environment."""
    if Environment.DEV_ENV:
        return APIUrls.DEV_URL
    elif Environment.STAGE_ENV:
        return APIUrls.STAGE_URL
    else:
        raise ValueError('Unsupported environment')


@pytest.fixture(
    params=[
        (APITokens.DATA_ENGINEER_TOKEN, 'data_engineer'),
        (APITokens.PROJECT_MANAGER_TOKEN, 'project_manager'),
        (APITokens.SITE_IM_PERSON_TOKEN, 'site_im_person'),
        (APITokens.NOT_VALID_TOKEN, 'not_valid_token'),
    ],ids=[
        'data_engineer', 'project_manager', 'site_im_person', 'not_valid_token'
    ],
    scope='session'
)
def api_client(request, api_url: str) -> APIClient:
    """
    Fixture for creating an APIClient instance with different roles (tokens).

    :param request: The request object containing the parameters for each role.
    :param api_url: string with URL

    :return APIClient: An instance of the APIClient class with the specified token and role.
    """
    token, role = request.param
    client = APIClient(token, role, api_url)
    return client


@pytest.fixture(scope="session")
def api_client_data_engineer(api_url: str) -> APIClient:
    """
    Fixture for creating an APIClient instance with data engineer role.

    :param api_url: string with URL

    :return APIClient: An instance of the APIClient class with data engineer role.
    """
    client = APIClient(APITokens.DATA_ENGINEER_TOKEN, "data_engineer", api_url)
    return client


@pytest.fixture(scope='session')
def test_data() -> dict:
    """Collect test data from YAML file."""
    return read_yaml_file(ConstantPaths.PATH_TEST_DATA)


@pytest.fixture()
def moerdijk_test_data(test_data: dict):
    """Collect test data for Moerdijk."""
    return test_data.get("sites").get("Moerdijk")
