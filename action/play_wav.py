"""
play_wav.py
"""
import os
import wave

import requests

from action.action import Action
from api.wav_endpoint import WavEndpoint
from config import AUDIO_OUTPUT_MATCH_SUBSTRING
import util.logger as logger

class PlayWav(Action):
    """
    Class to represent a play wav action.
    """

    def __init__(self, payload):
        super().__init__(PlayWav, payload)

        if 'record_id' not in payload:
            raise ValueError('Record ID not provided in payload')

        self.url = WavEndpoint().url(payload['record_id'], 'wav')

    def match_device(self, p, match_substring):
        """
        Get the device to play the wav file.
        """
        num_devices = p.get_device_count()
        for i in range(num_devices):
            device_info = p.get_device_info_by_index(i)
            if match_substring.lower() in device_info['name'].lower():
                return device_info
        raise ValueError(f'No audio device found with substring: {match_substring}')

    def execute(self, state):
        """
        Execute the play wav action.
        """
        response = requests.get(self.url, timeout=5)

        if response.status_code != 200:
            raise requests.exceptions.RequestException(
                f'Illegal status code: {response.status_code}'
            )

        file_path = 'tmp/play.wav'
        with open(file_path, 'wb') as f:
            f.write(response.content)

        # Open the wav file
        wf = wave.open(file_path, 'rb')

        # get pyaudio
        p = state.pyaudio()

        _format = p.get_format_from_width(wf.getsampwidth())
        _channels = wf.getnchannels()
        _device_info = self.match_device(p, AUDIO_OUTPUT_MATCH_SUBSTRING)
        _rate = int(_device_info['defaultSampleRate'])

        logger.debug(
            f'format={_format} channels={_channels} rate={_rate} device={_device_info["name"]}'
        )

        # Open PyAudio stream
        stream = p.open(
            format=_format,
            channels=_channels,
            rate=_rate,
            output=True,
            output_device_index=_device_info['index']
        )

        # Play the wav file
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # Close PyAudio stream
        stream.stop_stream()
        stream.close()

        # Remove the temporary wav file
        os.remove(file_path)
