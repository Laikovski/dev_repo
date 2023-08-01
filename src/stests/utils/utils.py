"""Utils and helpers for tests."""
import logging
import os

import yaml


def read_yaml_file(path_to_file: str) -> dict | None:
    """Return python dict object from YAML by path.

    :param path_to_file: relative path to the YAML file from the location of this script
    """
    try:
        script_directory = os.path.dirname(
            os.path.abspath(__file__).replace('utils', ''),
        )
        absolute_path = os.path.join(script_directory, path_to_file)
        logging.info(f'Get File by path {absolute_path}')
        with open(absolute_path) as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logging.error(
            f'File by path {os.path.abspath(absolute_path)} not found!',
        )
        return None
