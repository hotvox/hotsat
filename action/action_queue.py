"""
action_queue.py
"""
import util.logger as logger

from action.action import Action

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
        self.queue.append(action)

    def pop(self):
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
                action.execute(state)
            # pylint: disable=broad-except
            except Exception as e:
                logger.error(f'Error executing action: {action.klass.__name__} with payload: {action.payload}', e)
