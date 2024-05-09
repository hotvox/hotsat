"""
action_queue.py
"""
from util import logger
from action.action import Action
from api.action_endpoint import ActionEndpoint

class ActionQueue:
    """
    Class to represent a queue of actions.
    """

    def __init__(self):
        self.queue = []

    def add(self, action : Action):
        """
        Add an action to the queue.
        """
        logger.debug(f'Queueing action: {action.klass.__name__} with payload: {action.payload}')
        self.queue.append(action)

    def pop(self) -> Action:
        """
        Pop an action from the queue.
        """
        return self.queue.pop(0)

    def execute(self, state):
        """
        Execute all actions in the queue.
        """
        while len(self.queue) > 0:
            action = self.pop()
            logger.info(f'Executing action: {action.klass.__name__} with payload: {action.payload}')

            try:
                # delete the action from the server but keep it in memory
                ActionEndpoint().delete(action.payload['id'])

                action.execute(state)
            # pylint: disable=broad-except
            except Exception as e:
                logger.error(
                    f'Error executing: {action.klass.__name__} with payload: {action.payload}',
                    e
                )
