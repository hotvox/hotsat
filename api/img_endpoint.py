'''
img_endpoint.py
'''

from api.endpoint import Endpoint

class ImgEndpoint(Endpoint):
    """
    API endpoint for img files.
    """

    def __init__(self):
        super().__init__('/img')
