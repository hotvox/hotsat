"""
display_img.py
"""

import subprocess
import requests

from action.action import Action
from api.img_endpoint import ImgEndpoint

class DisplayImg(Action):
    """
    Class to represent an action to display an image.
    """

    def __init__(self, action_id, payload):
        super().__init__(DisplayImg, action_id, payload)
        self.record_id = payload['record_id']
        self.format = payload['format']
        self.url = ImgEndpoint().url(payload['record_id'], payload['format'])


    def execute(self, state):
        """
        Execute the action with the payload.
        """
        response = requests.get(self.url, timeout=5)

        if response.status_code != 200:
            raise requests.exceptions.RequestException(
                f'Illegal status code: {response.status_code}'
            )

        file_path = f'tmp/display.{self.format}'
        with open(file_path, 'wb') as f:
            f.write(response.content)

        # use fbi to display image
        subprocess.run(
            [
                'fbi',
                '-d', '/dev/fb0',
                '-T', '1',
                '-noverbose',
                '-a',
                file_path
            ],
            check=True
        )
        return []
