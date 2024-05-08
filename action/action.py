"""
action.py
"""

from api.endpoint import ActionEndpoint

class Action:
    """
    Class to represent an action that can be held in a queue.
    """

    def __init__(self, klass, payload):
        self.klass = klass
        self.payload = payload

    def execute(self, state):
        """
        Execute the action with the payload.
        """
        raise NotImplementedError

    def delete(self):
        """
        Delete the action.
        """
        ActionEndpoint().delete(self.payload['id'])
