'''
wav_endpoint.py
'''

from api.endpoint import Endpoint

class WavEndpoint(Endpoint):
    """
    API endpoint for wav files.
    """

    def __init__(self):
        super().__init__('/wav_output')
