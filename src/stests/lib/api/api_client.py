"""Module for api client."""
import os

import requests


import os
import requests

class APIClient:
    DEV_URL = 'https://dummyapi.io/data/v1'
    STAGE_URL = ''
    TEST_ENVIRONMENT = os.getenv('TEST_ENVIRONMENT')
    BASE_URL = STAGE_URL if TEST_ENVIRONMENT == 'stage' else DEV_URL
    API_METHODS = ('get', 'put', 'post', 'delete', 'patch')
    API_KEY = os.getenv("api_key")
    session = requests.Session()

    def __init__(self):
        """Initialize the object."""

    def update_headers(self, headers: dict, method: str):
        """Update headers based on the API method and environment."""
        if method in self.API_METHODS:
            if self.TEST_ENVIRONMENT == 'dev':
                user_auth = {"app-id": self.API_KEY}
            else:
                user_auth = {"app-id": self.API_KEY}
            headers.update(user_auth)

    def send_request(self, method: str, endpoint: str, data: dict = None, params: dict = None,
                     files: dict = None, headers: dict = None, url: str = BASE_URL) -> requests.Response:
        """Send API request."""
        if headers is None:
            headers = {}
        self.update_headers(headers, method)
        request = requests.Request(method, f"{url}{endpoint}", json=data, params=params,
                                   headers=headers, files=files)
        prepared_request = request.prepare()
        # self.session.verify = False
        response = self.session.send(prepared_request, timeout=10)
        return response
