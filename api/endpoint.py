"""
rest.py
"""
import requests

from config import API_URL
from util import logger
import validators

class Endpoint:
    """
    Class to represent an API endpoint.

    Attributes:
        path (str): The path of the endpoint.
    """

    def __init__(self, path : str):
        self.path = path

        # Validate that the path is not None
        if self.path is None:
            raise ValueError('Path must not be None')

        # Validate that the path is a string
        if not isinstance(self.path, str):
            raise ValueError('Path must be a string')

        # Validate that the path starts with a /
        if not self.path.startswith('/'):
            raise ValueError('Path must start with /')

        # Validate that the path does not end with a /
        if self.path.endswith('/'):
            raise ValueError('Path must not end with /')

    def url(self, record_id : int | None = None, ext : str = 'json'):
        """
        Returns the full URL of the endpoint.
        """
        result = None
        if record_id is not None:
            result = f'{API_URL}{self.path}/{record_id}.{ext}'
        else:
            result = f'{API_URL}{self.path}.{ext}'
        if not validators.url(result):
            raise ValueError(f'Invalid URL: {result}')
        logger.debug(f'Built URL: {result}')
        return result

    def headers(self):
        """
        Returns a dictionary of standard headers.
        """
        return {
            'x-mac-address': '00:00:00:00:00:00',
        }

    def get(self, record_id : int = None):
        """
        Perform a GET request.

        Args:
            id (int): The ID of the object to get.

        Returns:
            dict: The response from the server.
        """
        response = requests.get(
            self.url(record_id),
            headers=self.headers(),
            timeout=5
        )
        return response.json()

    def delete(self, record_id : int):
        """
        Perform a DELETE request.

        Args:
            id (int): The ID of the object to delete.

        Returns:
            dict: The response from the server.
        """
        response = requests.delete(
            self.url(record_id),
            headers=self.headers(),
            timeout=5
        )
        return response.json()
