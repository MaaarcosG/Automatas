from Thompson.tree import *
from Thompson.operations import *

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
        self.accept = True

class Handler:
    def __init__(self, symbol, id):
        self.symbol = symbol
        self.id = id

def automata(tree, expresion):
    data = Automata(expresion)
    start, finish = transition_handler(tree, data)
    
    return data

        