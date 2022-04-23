def hello_world(i: int = 0) -> str:
    "Doc String"
    print("hello world")
    return "string"


def good_night() -> str:
    print("good night")
    return "string"


def hello_goodbye():
    hello_world("x")
    good_night()
