"""Asserts for API tests."""
from requests import Response


def check_verify_response_status_code(actual_status_code: Response, expected_status_code: int = 200):
    """
    Check if the response has the expected status code.

    Parameters:
        actual_status_code: The response object to check.
        expected_status_code (int, optional): The expected status code to check against.
            Defaults to 200.

    :return: bool: True if the response status code matches the expected status code or is 200,
              False otherwise.
    """
    return expected_status_code == actual_status_code


def check_verify_json_not_empty(response: Response):
    """
    Check if the JSON response is not empty and contains information.

    :param response: The JSON response from the API.
    :type response: dict
    :return: True if the JSON response contains information, False otherwise.
    :rtype: bool
    """
    return isinstance(response, dict) and len(response) > 0
