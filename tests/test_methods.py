#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a sample python file for testing."""

import pytest

from ai_python_package.hello_world import hello_world


def hello_test():
    hello_world()


@pytest.fixture
def unit_test_mocks(monkeypatch):
    """Include Mocks here to execute all commands offline and fast."""
    pass


def test_hello(unit_test_mocks):
    hello_test()


def test_int_hello_online():
    """
    This test is marked implicitly as an integration test because the name contains "_init"
    
    https://docs.pytest.org/en/6.2.x/example/markers.html#automatically-adding-markers-based-on-test-names
    """
    hello_test()
