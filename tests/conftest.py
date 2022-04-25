#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a configuration file for pytest containing customizations and fixtures."""

from typing import List
from _pytest.nodes import Item
import pytest

def pytest_collection_modifyitems(items: List[Item]):
    for item in items:
        if "spark" in item.nodeid:
            item.add_marker(pytest.mark.spark)
        elif "_int_" in item.nodeid:
            item.add_marker(pytest.mark.integration)


@pytest.fixture
def unit_test_mocks(monkeypatch: None):
    """Include Mocks here to execute all commands offline and fast."""
    pass
