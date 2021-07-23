def hello_world(i: int = 0) -> str:
    "Doc Stringz"
    print("hello world")


def good_night():
    print("good night")
    return

    
def hello_goodbye():
    hello_world("x")
    good_night()
