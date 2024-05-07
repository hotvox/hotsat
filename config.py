"""
config.py
"""
import os

API_PROTOCOL=os.getenv("API_PROTOCOL", "http")
API_HOST=os.getenv("API_HOST", "192.168.42.1")
API_PORT=os.getenv("API_PORT", "80")
API_VERSION=os.getenv("API_VERSION", "v1")
API_URL = f"{API_PROTOCOL}://{API_HOST}:{API_PORT}/api/{API_VERSION}"

AUDIO_OUTPUT_MATCH_SUBSTRING=os.getenv("AUDIO_OUTPUT_MATCH_SUBSTRING", "Anker")
