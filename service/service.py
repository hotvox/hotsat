"""
service.py
"""
class Service:
    """
    Abstract class to represent a service.
    """

    def __init__(self, klass, state):
        self.klass = klass
        self.state = state

    def run(self):
        """
        Run the service for one iteration.
        This method should be overridden by the subclass.

        Raises:
            NotImplementedError: If the subclass does not override this method.

        Returns:
            Action[]: A list of actions to be executed.
        """
        raise NotImplementedError
