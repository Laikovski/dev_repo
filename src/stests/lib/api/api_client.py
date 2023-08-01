"""Module for api client."""
import logging
from typing import Optional

import requests


class APIClient:
    """Init class APIClient."""

    API_METHODS = ('get', 'put', 'post', 'delete', 'patch')

    def __init__(self, token: str, role: str, url: str):
        """Initialize the object."""
        self.token = token
        self.role = role
        self.session = requests.Session()
        self.url = url

    def update_headers(self, headers: dict, method: str):
        """Update headers based on the API method and environment."""
        if method in self.API_METHODS:
            user_auth = {'app-id': self.token}
            headers.update(user_auth)

    def send_request(
        self, method: str, endpoint: str, data: dict = {}, params: dict = {},
        files: dict = {}, headers: dict = {}, url: Optional[str] = None,
    ) -> requests.Response:
        """Send API request."""
        url = url or self.url
        self.update_headers(headers, method)
        request = requests.Request(
            method, f'{url}{endpoint}', json=data, params=params,
            headers=headers, files=files,
        )
        prepared_request = request.prepare()
        # self.session.verify = False
        response = self.session.send(prepared_request, timeout=10)
        logging.info(
            f'Response received successful - {endpoint}, - {response.status_code}',
        )

        return response
