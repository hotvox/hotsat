"""
rest.py
"""
import requests

from config import API_URL

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

    def url(self, record_id : int = -1, ext : str = 'json'):
        """
        Returns the full URL of the endpoint.
        """
        if record_id != -1:
            return f'{API_URL}{self.path}/{record_id}.{ext}'

        return f'{API_URL}{self.path}.{ext}'

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
