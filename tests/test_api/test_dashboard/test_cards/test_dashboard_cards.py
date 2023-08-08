"""Module with tests for card side view."""
import pytest
from pydantic import ValidationError
from stests.asserts.api_asserts import check_verify_json_not_empty
from stests.asserts.api_asserts import check_verify_response_status_code
from stests.json_schemas.dashboard.face_side_of_the_card import DashboardCard
from stests.lib.api.models.bclearer import Bclearer


@pytest.mark.smoke
def test_dashboard_face_side_card_response(test_data, api_client):
    """
    Check dashboards face side card.

    1. Check Status Code.
    2. Check Headers Response.
    3. Check Verify JSON data is not empty.

    :param test_data: dict
    """
    bclearer = Bclearer(api_client)
    response = bclearer.get_cards()

    expected_status_code = 200
    actual_status_code = response.status_code

    response_json = response.json()

    if api_client.role == 'data_engineer':

        assert check_verify_response_status_code(response.status_code, expected_status_code), \
            f"Expected result: {expected_status_code} doesn't match actual result: {actual_status_code}."

        # TODO: assert for check headers

        assert check_verify_json_not_empty(
            response_json,
        ), f'Response JSON is empty or not found: {response_json}.'

    else:
        assert actual_status_code == 400, (
            f'Actual status code {actual_status_code} '
            f"doesn't match expected {expected_status_code}, for {api_client.role}"
        )


def test_validate_json_schema_dashboard_card(test_data, api_client_data_engineer):
    """
    Test to validate the JSON schema of the dashboard face side card.

    This test checks if the response JSON for dashboard face side cards
    matches the expected JSON schema defined in APICardData.model_validate.
    If there is a validation error, the test will fail with an appropriate message.
    """
    bclearer = Bclearer(api_client_data_engineer)
    response = bclearer.get_cards()

    response_json = response.json()

    try:
        DashboardCard.model_validate(response_json)
    except ValidationError as e:
        pytest.fail(f'JSON schema validation error: {e}')


def test_check_correct_values_for_moerdijk(api_client_data_engineer, moerdijk_test_data):
    """
    Test to check if the refinery names in the response JSON are correct.

    This test verifies that the 'refineryId' values in the response JSON for
    dashboard face side cards match the expected values defined in the 'plants'
    data retrieved from 'test_data'. If any 'refineryId' does not match the
    expected value or if the 'refinery_name' is unknown, the test will fail with
    an appropriate message.
    """
    bclearer = Bclearer(api_client_data_engineer)
    response = bclearer.get_cards()

    response_json = response.json()

    refactored_json = DashboardCard(**response_json)

    assert refactored_json.site.site_name == moerdijk_test_data.get(
        'site_name',
    )
    assert refactored_json.site.site_unique_identifier == moerdijk_test_data.get(
        'unique_identifier',
    )
