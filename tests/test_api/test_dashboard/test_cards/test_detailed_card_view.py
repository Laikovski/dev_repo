"""Module with tests for card side view."""
import pytest
from pydantic import ValidationError
from stests.asserts.api_asserts import check_verify_json_not_empty
from stests.asserts.api_asserts import check_verify_response_status_code
from stests.config.constants import APIRoutes
from stests.json_schemas.dashboard.schema_detail_card import DetailCardResponse
from stests.lib.api.models.bclearer import Bclearer

from stests.lib.api.models.mock_bclearer import MockAPIClient


@pytest.mark.smoke
def test_dashboard_card_detail_view_response(test_data):
    """
    Check dashboards face side card.

    1. Check Status Code.
    2. Check Headers Response.
    3. Check Verify JSON data is not empty.

    :param test_data: dict
    """
    plants = test_data.get('plants')
    refinery_id = plants.get('Moerdijk')

    mock_api_client = MockAPIClient()
    response = mock_api_client.get_card_detail_view(
        APIRoutes.DETAIL_CARD, refinery_id=refinery_id,
    )

    expected_status_code = 200
    actual_status_code = response.status_code

    response_json = response.json

    assert check_verify_response_status_code(response.status_code, expected_status_code), \
        f"Expected result: {expected_status_code} doesn't match actual result: {actual_status_code}."

    # TODO: assert for check headers

    assert check_verify_json_not_empty(
        response_json,
    ), f'Response JSON is empty or not found: {response_json}.'


def test_validate_json_schema_detail_card(test_data, api_client):
    """
    Test to validate the JSON schema of the dashboard detail card.

    This test checks if the response JSON for dashboard detail card
    matches the expected JSON schema defined in APICardData.model_validate.
    If there is a validation error, the test will fail with an appropriate message.
    """
    refinery_id = test_data.get('plants')['Moerdijk']

    mock_api_client = MockAPIClient()
    response = mock_api_client.get_card_detail_view(
        APIRoutes.DETAIL_CARD, refinery_id=refinery_id,
    )

    bCLERAer = Bclearer(api_client)
    bCLERAer.get_card_detail_view(refinery_id=123)

    response_json = response.json

    try:
        DetailCardResponse.model_validate(response_json)
    except ValidationError as e:
        pytest.fail(f'JSON schema validation error: {e}')
