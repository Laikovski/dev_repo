"""Collect all fixtures."""
from __future__ import annotations

import pytest

from src.stests.config.constants import ConstantPaths
from src.stests.utils.utils import read_yaml_file


@pytest.fixture(scope='session')
def get_test_data():
    """Collect test data from YAML file."""
    return read_yaml_file(ConstantPaths.PATH_TEST_DATA)
