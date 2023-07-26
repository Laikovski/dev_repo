"""Class contains Bclearer MVP Object."""
from __future__ import annotations

from stests.lib.api.api_client import APIClient  # type: ignore


class Bclearer:
    """Object bCLEARer."""

    def __init__(self):
        """Init object."""
        self.api_client = APIClient()

    def get_data(self):
        """Get data method."""
        return self.api_client.send_request(method='get', endpoint='/user')

    def get_user(self, user_id):
        """Get User method."""
        return self.api_client.send_request(method='get', endpoint=f'/users/{user_id}')

    def update_user(self, user_id, user_data):
        """Update User method."""
        return self.api_client.send_request(method='put', endpoint=f'/users/{user_id}', data=user_data)

    def delete_user(self, user_id):
        """Delete User method."""
        return self.api_client.send_request(method='delete', endpoint=f'/users/{user_id}')
