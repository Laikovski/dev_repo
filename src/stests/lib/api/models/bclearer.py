"""Class contains Bclearer MVP Object."""
from src.stests.lib.api.api_client import APIClient


class Bclearer:
    def __init__(self):
        self.api_client = APIClient()

    def get_data(self, ):
        return self.api_client.send_request(method='get', endpoint='/user')

    def get_user(self, user_id):
        return self.api_client.send_request(method='get', endpoint=f'/users/{user_id}')

    def update_user(self, user_id, user_data):
        return self.api_client.send_request(method='put', endpoint=f'/users/{user_id}', data=user_data)

    def delete_user(self, user_id):
        return self.api_client.send_request(method='delete', endpoint=f'/users/{user_id}')