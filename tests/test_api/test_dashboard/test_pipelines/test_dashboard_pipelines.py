"""Test pipelines."""
import pytest
from stests.asserts.api_asserts import check_verify_json_not_empty
from stests.asserts.api_asserts import check_verify_response_status_code
from stests.config.constants import APIRoutes

from src.stests.lib.api.models.mock_bclearer import MockAPIClient


@pytest.mark.smoke
@pytest.mark.skip('refactor and run all pipelines in parallel')
def test_run_pipeline_succesful(test_data: dict):
    """
    Check dashboards face side card.

    1. Check Status Code.
    2. Check Headers Response.
    3. Check Verify JSON data is not empty.

    :param test_data: dict
    """
    mock_api_client = MockAPIClient()
    response = mock_api_client.run_pipeline(
        APIRoutes.RUN_PIPELINE, refinery_id='test', pipeline_id='test',
    )

    expected_status_code = 200
    actual_status_code = response.status_code

    response_json = response.json

    assert check_verify_response_status_code(actual_status_code, expected_status_code), \
        f'Expected status code: {expected_status_code}, but got: {actual_status_code}.'

    # TODO: assert for check headers (Add appropriate assertion for headers)

    assert check_verify_json_not_empty(
        response_json,
    ), f'Response JSON is empty or not found: {response_json}.'


@pytest.mark.skip(reason='Not implemented')
def test_run_pipeline_missing_fields(test_data):
    """Negative test for checking response with missing required fields in the request.

    Steps:
        1. Send a request to run a pipeline without filling in the required fields 'refinery_id' and 'pipeline_id'.
        2. Check the response status code is 400.
        3. Check that the response contains the expected error message for missing fields.

    Args:
        test_data (dict): Test data containing JSON payloads for different test scenarios.

    Raises:
        AssertionError: If any of the checks fail.
    """
    mock_api_client = MockAPIClient()

    response = mock_api_client.run_pipeline(APIRoutes.RUN_PIPELINE)

    expected_status_code = 400
    actual_status_code = response.status_code

    response_json = response.json

    assert check_verify_response_status_code(actual_status_code, expected_status_code), \
        f'Expected status code: {expected_status_code}, but got: {actual_status_code}.'

    expected_error_message = 'Some required fields are missing in the request.'
    assert response_json.get('error') == expected_error_message, \
        f"Expected error message: '{expected_error_message}' not found in response: {response_json}."


@pytest.mark.skip(reason='Not implemented')
def test_run_pipeline_invalid_pipeline_id():
    """Negative test for handling invalid pipeline ID in /run_pipeline.

    Steps:
        1. Send a request to run a pipeline with an invalid 'pipeline_id' field.
        2. Check the response status code is 400.
        3. Check that the response contains the expected error message for invalid 'pipeline_id' field.

    Raises:
        AssertionError: If any of the checks fail.
    """
    mock_api_client = MockAPIClient()

    response = mock_api_client.run_pipeline(
        APIRoutes.RUN_PIPELINE, refinery_id='test', pipeline_id='test',
    )
    expected_response = {
        'status': 'error',
        'message': '',
    }

    assert response == expected_response, f'Unexpected response: {response}'
