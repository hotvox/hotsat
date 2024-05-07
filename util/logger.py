"""
logger.py
"""

from datetime import datetime
import traceback

ANSI_RESET = "\033[0m"
ANSI_BLUE = "\033[34m"
ANSI_GREEN = "\033[32m"
ANSI_RED = "\033[31m"
ANSI_YELLOW = "\033[33m"
ANSI_FAILURE = "\033[91m"

def _log(message, ansi_color):
    """
    Log a message to the console.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {ansi_color}{message}{ANSI_RESET}")

def debug(message):
    """
    Log a debug message to the console.
    """
    _log(message, ANSI_BLUE)

def info(message):
    """
    Log a message to the console.
    """
    _log(message, ANSI_GREEN)

def error(message, exception=None):
    """
    Log an error to the console
    """
    _log(message, ANSI_RED)
    if exception:
        print(ANSI_FAILURE  + traceback.format_exc() + ANSI_RESET)

def warn(message, exception=None):
    """
    Log a warning to the console
    """
    _log(message, ANSI_YELLOW)
    if exception:
        print(ANSI_FAILURE  + traceback.format_exc() + ANSI_RESET)
