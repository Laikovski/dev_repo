"""Class contains bCLEARer MVP Object."""
import logging

from src.stests.config.constants import APIRoutes


class Bclearer:
    """Object bCLEARer."""

    def __init__(self, api_client):
        """Init object."""
        self.api_client = api_client

    def get_test_key(self):
        """Get data cards."""
        logging.info(f'Send request to endpoint - {APIRoutes.CARDS}')

        return self.api_client.send_request(method='get', endpoint='/user')

    def get_cards(self):
        """Get data cards."""
        logging.info(f'Send request to endpoint - {APIRoutes.CARDS}')

        return self.api_client.send_request(method='post', endpoint=APIRoutes.CARDS)

    def get_card_detail_view(self, refinery_id: int):
        """Get card detail view."""
        logging.info(f'Send request to endpoint - {APIRoutes.DETAIL_CARD}')
        data = {
            'refineryId': refinery_id,
        }
        return self.api_client.send_request(method='get', endpoint=APIRoutes.DETAIL_CARD, data=data)
