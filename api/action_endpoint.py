"""
action_endpoint.py
"""
from api.endpoint import Endpoint

class ActionEndpoint(Endpoint):
    """
    API endpoint for actions.
    """

    def __init__(self):
        super().__init__('action')
