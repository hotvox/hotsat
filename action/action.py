"""
action.py
"""

class Action:
    """
    Class to represent an action that can be held in a queue.
    """

    def __init__(self, klass, action_id, payload):
        # ensure klass, action_id, and payload are set
        if not klass:
            raise ValueError('klass must be set')

        if not action_id:
            raise ValueError('action_id must be set')

        if not payload:
            raise ValueError('payload must be set')

        self.action_id = action_id
        self.klass = klass
        self.payload = payload

    def execute(self, state):
        """
        Execute the action with the payload.
        """
        raise NotImplementedError

    def __str__(self):
        return f'id={self.action_id}, klass={self.klass}, payload={self.payload}'
