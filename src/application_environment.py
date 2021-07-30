import logging

from pathlib import Path
from os import environ


class ApplicationEnvironment:

    # Constants
    SPOTIFY_CLIENT_ID_ENV_VAR='SPOTIFY_CLIENT_ID'
    SPOTIFY_CLIENT_SECRET_ENV_VAR='SPOTIFY_CLIENT_SECRET'
    SPOTIFY_REDIRECT_URI_ENV_VAR='SPOTIFY_REDIRECT_URI'

    # Constructors
    def __init__(self):
        self.__createLogDirectory()
        logging.basicConfig(filename="log/sonar_login_provider.log", level=logging.DEBUG)

        self.client_id = self.__set_env_var(self.SPOTIFY_CLIENT_ID_ENV_VAR)
        self.client_secret = self.__set_env_var(self.SPOTIFY_CLIENT_SECRET_ENV_VAR)
        self.redirect_uri = self.__set_env_var(self.SPOTIFY_REDIRECT_URI_ENV_VAR)

    # region Public Methods
    def env_vars_are_set(self):
        return self.client_id != "" and self.client_secret != "" and self.redirect_uri != ""

    # region Helper Methods
    def __createLogDirectory(self):
        Path("log").mkdir(exist_ok=True)

    def __set_env_var(self, env_var):
        env_var_value = environ.get(env_var)
        if env_var_value is None:
            logging.error(f'{env_var} environment variable is not set...')
            return ""

        return env_var_value
