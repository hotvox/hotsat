"""
Entry point for the output daemon.
"""
from time import sleep

from action.action_queue import ActionQueue
from service.service import Service
from service.puppet_service import PuppetService
from util import logger
from util.state import State
from pyaudio import PyAudio

if __name__ == "__main__":
    try:
        logger.info('Starting output daemon...')
        state = State()
        state.create_singleton('action_queue', ActionQueue)
        state.create_singleton('pyaudio', PyAudio)
        while True:
            services : list[Service] = [
                PuppetService
            ]
            for service in services:
                s = service(state)
                logger.info(f'Running service: {s.klass.__name__}')
                try:
                    s.run()
                except Exception as e:
                    logger.error(f'Error running service: {s.klass.__name__}', e)

            state.action_queue().execute(state)
            sleep(1)

    except KeyboardInterrupt:
        logger.warn('Keyboard interrupt received')
    finally:
        state.pyaudio().terminate()
        logger.info('Terminated pyaudio')
        logger.info('Exiting...')
