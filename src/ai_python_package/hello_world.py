#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a Sample Python file"""

def hello_world(i: int = 0) -> str:
    """Doc String"""
    print("hello world")
    return f"string-{i}"


def good_night() -> str:
    """Doc String"""
    print("good night")
    return "string"


def hello_goodbye():
    """Doc String"""
    hello_world("x")
    good_night()
