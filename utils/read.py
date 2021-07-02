import os
from utils.error import FileNotFound, NoDataError
import json

config_file = "config.json"


def read_config():
    config_path = os.getcwd() + "\\" + config_file
    print(config_path)
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        return config_data
    else:
        raise FileNotFound(config_path)


def get_config(name):
    config_data = read_config()
    if config_data == "" or config_data.get(name) is None:
        raise NoDataError(name)
    return config_data.get(name)


