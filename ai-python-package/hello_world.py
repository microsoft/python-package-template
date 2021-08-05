def hello_world(i: int = 0) -> str:
    "Doc Stringz"
    print("hello world")


def good_night():
    print("good night")
    return

    
def hello_goodbye():
    """
    Little Doc String
    """
    hello_world("x")
    good_night()

    
class Greetings:
    def __init__(input):
        self.Input = input
        
    def getInput(self):
        return self.Input
    
    def bigAdd(self):
        return self.Input + self.Input + self.Input + self.Input + self.Input+ self.Input+ self.Input+ self.Input+ self.Input+ self.Input+ self.Input + self.Input + self.Input+ self.Input
