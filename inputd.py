"""
Entry point for the input daemon.
"""
from time import sleep

from util import logger
from util.state import State

if __name__ == "__main__":
    try:
        logger.info('Starting input daemon...')
        state = State()
        while True:
            sleep(1)

    except KeyboardInterrupt:
        logger.warn('Keyboard interrupt received')
    finally:
        logger.info('Exiting...')
