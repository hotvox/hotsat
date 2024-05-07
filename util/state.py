"""
state.py
"""
import util.logger as logger

class State:
    """
    Class to represent the state of the system.
    """

    def __init__(self):
        self.state = {}

    def set(self, key, value, klass):
        """
        Set a key value pair in the state.
        """

        # Validate that the value being set is of the correct type
        # Allow None values regardless of type
        if value is not None and not isinstance(value, klass):
            raise ValueError(f'Value {value} is not of type {klass}')

        self.state[key] = value

    def get(self, key, klass):
        """
        Get a value from the state.
        """
        value = self.state.get(key)

        # Validate that the value is of the correct type
        # Allow None values regardless of type
        if value is not None and not isinstance(value, klass):
            raise ValueError(f'Value {value} is not of type {klass}')

        return value

    def clear(self):
        """
        Clear the state.
        """
        self.state.clear()

    def create_singleton(self, key, klass):
        """
        Define a singleton in the state.
        """
        logger.debug(f'Creating singleton: {key}')
        self.set(key, klass(), klass)
        setattr(self, key, lambda: self.get(key, klass))

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return str(self.state)

    def __eq__(self, other):
        return self.state == other.state
