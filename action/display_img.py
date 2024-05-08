"""
display_img.py
"""

import subprocess

from action.action import Action
from api.img_endpoint import ImgEndpoint

class DisplayImg(Action):
    """
    Class to represent an action to display an image.
    """

    def __init__(self, payload):
        super().__init__(DisplayImg, payload)

        if 'url' not in payload:
            raise ValueError('URL not provided in payload')

        self.url = ImgEndpoint().url(payload['record_id'], payload['format'])


    def execute(self, state):
        """
        Execute the action with the payload.
        """
        subprocess.run(
            [
                'feh',
                '--force-aliasing',
                '--auto-zoom',
                '--borderless',
                '--hide-pointer',
                '--fullscreen',
                '--image-bg', 'black',
                self.url
            ],
            check=True
        )
        return []
