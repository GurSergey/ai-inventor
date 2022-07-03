from pyaml_env import parse_config

config = parse_config('config.yml')


def get_config() -> dict:
    """
    Method return dictionary of config
    :return: dict
    """
    return config
