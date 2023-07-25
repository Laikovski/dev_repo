"""Utils and helpers for tests."""
import logging
import os
from typing import Optional

import yaml


def read_yaml_file(path_to_file: str) -> Optional[dict]:
    """Return python dict object from Yaml by path.

    :param path_to_file: path to YAML file
    """
    try:
        absolute_path = os.path.abspath(path_to_file)
        logging.info(f'Get File by path {absolute_path}')
        with open(absolute_path) as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logging.error(f'File by path {path_to_file} not found!')
        return None
