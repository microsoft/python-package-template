#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a sample python file for testing."""
from ai_python_package.hello_world import hello_world


def hello_test():
    """
    This defines the expected usage, which can then be used in various test cases.
    """
    hello_world()


def test_hello(unit_test_mocks):
    """
    This is a simple test, which can use a mock to override online functionality.
    """
    hello_test()


def test_int_hello_online():
    """
    This test is marked implicitly as an integration test because the name contains "_init_"
    
    https://docs.pytest.org/en/6.2.x/example/markers.html#automatically-adding-markers-based-on-test-names
    """
    hello_test()
