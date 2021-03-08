# to create the automata
class Automata:
    def __init__(self, expresion):
        self.expresion = expresion
        self.state = []

class State:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        # transition list
        self.transition = []
        # is it accept transition
        self.accept = False

class Handler:
    def __init__(self, symbol, id):
        self.symbol = symbol
        self.id = id

        