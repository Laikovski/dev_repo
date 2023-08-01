"""Module with tests for card side view."""
import pytest
from pydantic import ValidationError
from stests.asserts.api_asserts import check_verify_json_not_empty
from stests.asserts.api_asserts import check_verify_response_status_code
from stests.config.constants import APIRoutes
from stests.json_schemas.dashboard.face_side_of_the_card import APICardData
from stests.lib.api.models.bclearer import Bclearer

from src.stests.lib.api.models.mock_bclearer import MockAPIClient


@pytest.mark.smoke
def test_dashboard_face_side_card_response(test_data):
    """
    Check dashboards face side card.

    1. Check Status Code.
    2. Check Headers Response.
    3. Check Verify JSON data is not empty.

    :param test_data: dict
    """
    mock_api_client = MockAPIClient()
    response = mock_api_client.get_cards(APIRoutes.CARDS)

    expected_status_code = 200
    actual_status_code = response.status_code

    response_json = response.json

    assert check_verify_response_status_code(response.status_code, expected_status_code), \
        f"Expected result: {expected_status_code} doesn't match actual result: {actual_status_code}."

    # TODO: assert for check headers

    assert check_verify_json_not_empty(
        response_json,
    ), f'Response JSON is empty or not found: {response_json}.'


def test_validate_json_schema_cards(test_data):
    """
    Test to validate the JSON schema of the dashboard face side cards.

    This test checks if the response JSON for dashboard face side cards
    matches the expected JSON schema defined in APICardData.model_validate.
    If there is a validation error, the test will fail with an appropriate message.
    """
    mock_api_client = MockAPIClient()
    response = mock_api_client.get_cards(APIRoutes.CARDS)

    response_json = response.json

    try:
        APICardData.model_validate(response_json)
    except ValidationError as e:
        pytest.fail(f'JSON schema validation error: {e}')


def test_check_correct_refinery_names(test_data):
    """
    Test to check if the refinery names in the response JSON are correct.

    This test verifies that the 'refineryId' values in the response JSON for
    dashboard face side cards match the expected values defined in the 'plants'
    data retrieved from 'test_data'. If any 'refineryId' does not match the
    expected value or if the 'refinery_name' is unknown, the test will fail with
    an appropriate message.
    """
    mock_api_client = MockAPIClient()
    response = mock_api_client.get_cards(APIRoutes.CARDS)

    response_json = response.json

    plants = test_data.get('plants')

    for refinery in response_json['refineryDetails']:
        refinery_name = refinery['name']
        refinery_id = refinery['refineryId']

        if refinery_name in plants:
            expected_refinery_id = plants[refinery_name]
            assert refinery_id == expected_refinery_id, f"Invalid 'refineryId' value for '{refinery_name}'. " \
                                                        f'Expected: {expected_refinery_id}, Actual: {refinery_id}.'
        else:
            pytest.fail(f'Unknown refinery name: {refinery_name}')


def test_validate_key(test_data, api_client):
    """Here text."""
    bclearer = Bclearer(api_client)
    response = bclearer.get_test_key()
    response_json = response.status_code

    if api_client.role == 'data_engineer':
        assert response_json == 200
    else:
        assert response_json == 402
