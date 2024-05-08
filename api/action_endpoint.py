"""
action_endpoint.py
"""
from api.endpoint import Endpoint
from action.action import Action
from action.action_parse import parse_action

class ActionEndpoint(Endpoint):
    """
    API endpoint for actions.
    """

    def __init__(self):
        super().__init__('/actions')

    def get_actions(self) -> list[Action]:
        """
        Get all actions.

        Returns:
            dict: The response from the server.
        """
        json = self.get()

        actions = []
        for entry in json:
            # validate that the entry is a dictionary and has a klass and payload key
            if not isinstance(entry, dict):
                raise ValueError('Entry must be a dictionary')

            if 'klass' not in entry:
                raise ValueError('Entry must have a klass key')

            if 'payload' not in entry:
                raise ValueError('Entry must have a payload key')

            klass = parse_action(entry['klass'])
            payload = entry['payload']
            actions.append(klass(payload))

        return actions
