"""Mock client."""
import json
import logging
import os
from unittest.mock import Mock

from requests import Response

from src.stests.config.constants import APIRoutes


class MockAPIClient(Mock):
    """Mock Api Client."""

    def __init__(self, *args, **kwargs):
        """Init mock class client."""
        super().__init__(*args, **kwargs)
        file_path = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__),
            ), 'mock_test_data.json',
        )
        with open(file_path) as f:
            self.response_data = json.load(f)

        self.response = Response()
        self.response.status_code = 200

    def get_cards(self, path, **kwargs):
        """Get cards."""
        logging.info(f'Send request to endpoint /Mock - {APIRoutes.CARDS}')

        if path == '/get_cards':
            self.response.status_code = 200
            self.response.json = self.response_data['cards_response']
            logging.info(
                f'Response received successful /Mock - {APIRoutes.CARDS}',
            )
        else:
            self.response.status_code = 404
            self.response.json = {'error': 'Not Found'}
        return self.response

    def get_card_detail_view(self, path, refinery_id, **kwargs):
        """Get card details."""
        if path == '/card_detail_view' and refinery_id == 123:
            self.response.status_code = 200
            self.response.json = self.response_data['card_detail_view']
        else:
            self.response.status_code = 404
            self.response.json = {'error': 'Not Found'}
        return self.response

    def run_pipeline(self, path, refinery_id, pipeline_id=1, **kwargs):
        """Run pipeline."""
        if path == '/run_pipeline' and refinery_id == 123 and pipeline_id:
            self.response.status_code = 200
            self.response.json = self.response_data['run_pipeline']
        else:
            self.response.status_code = 404
            self.response.json = {'error': 'Not Found'}
        return self.response
