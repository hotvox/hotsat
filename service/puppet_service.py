"""
puppet_service.py
"""
from service.service import Service
from action.play_wav import PlayWav
from api.wav_endpoint import WavEndpoint
from api.action_endpoint import ActionEndpoint

class PuppetService(Service):
    """
    Class to represent a puppet service.
    """

    def __init__(self, state):
        super().__init__(PuppetService, state)

    def run(self):
        """
        Run the puppet service for one iteration.

        Returns:
            Action[]: A list of actions to be executed.
        """
        # self.state.action_queue().add(PlayWav({'url': WavEndpoint().url(0, 'wav')}))
        actions = ActionEndpoint().get_actions()
        for action in actions:
            self.state.action_queue().add(action)
