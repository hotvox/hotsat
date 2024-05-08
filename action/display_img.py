"""
display_img.py
"""

import subprocess
import validators

from action.action import Action

class DisplayImg(Action):
    """
    Class to represent an action to display an image.
    """

    def __init__(self, payload):
        super().__init__(DisplayImg, payload)

        if 'url' not in payload:
            raise ValueError('URL not provided in payload')

        if not validators.url(payload['url']):
            raise ValueError('Invalid URL provided in payload')

        # Check if the URL is a valid URL


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
                self.payload['url']
            ],
            check=True
        )
        return []
