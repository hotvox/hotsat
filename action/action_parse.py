'''
action_parse.py
'''

from action.action import Action
from action.play_wav import PlayWav
from action.display_img import DisplayImg

# given a string, return the corresponding action class
def parse_action(action_str : str) -> Action:
    """
    Parse an action string into an action class.

    Args:
        action_str (str): The action string to parse.

    Returns:
        Action: The action class corresponding to the action string.
    """
    if action_str == 'PlayWav':
        return PlayWav
    if action_str == 'DisplayImg':
        return DisplayImg
    raise ValueError(f'Invalid action string: {action_str}')