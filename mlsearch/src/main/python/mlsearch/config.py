import os

class Config(object):
    """Class for API Request configuration."""

    # Paper with code configuration
    PWC_USER_NAME = os.environ.get('PWC_USER_NAME') or ''
    PWC_PASSWORD = os.environ.get('PWC_PASSWORD') or ''
    PWC_URL = os.environ.get('PWC_URL') or "https://paperswithcode.com/api/v0/search/?q="

    # Github configuration
    GITHUB_ACC_TOKEN = os.environ.get('GITHUB_ACC_TOKEN') or None
    GITHUB_URL = os.environ.get('GITHUB_URL') or "in:readme+in:description"

    # AIP Source
    VALID_API_SOURCE = ['paperwithcode', 'github', 'coursera']