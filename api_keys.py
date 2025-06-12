import configparser as cp
from typing import Dict

class APIKey:
    def __init__(self, key: str):
        self._key = key

    def get(self):
        return self._key

    def __repr__(self):
        return "APIKey <REDACTED>"

    __str__ = __repr__

def load_api_keys(env_file: str = ".env.ini") -> Dict[str, APIKey]:
    config = cp.ConfigParser()
    config.read(env_file)
    return {key: APIKey(config["API_KEYS"][key]) for key in config["API_KEYS"]}

if __name__ == "__main__":
    print(load_api_keys())
