'''
    Convert Nodeterministic finite automatan (NFA) to Deterministic finite automatan (DFA)
'''

# to create the automata
from Thompson.nfa import Automata
from Thompson.nfa import Handler
from Thompson.nfa import State
# create collections
from collections import Counter

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
EPSILON = "ε"

# return the regular expresion
def get_symbol(automata):
    data_symbol = []
    for symbol in automata.expresion:
        if (symbol not in OPERATORS) and (symbol not in data_symbol) and (symbol != EPSILON):
            data_symbol.append(symbol)
    return data_symbol

# epsilon lock
def ecerradura(automata, current_node):
    # current node
    for node in current_node:
        for transition in automata.state[node].transition:
            # it found EPSILON and not have movement
            if (transition.symbol == EPSILON) and (transition.id not in current_node):
                current_node.append(transition.id)
    return current_node

# if the acceptance node is TRUE, if not False
def accept_node(tree, state):
    for node in state:
        if tree.state[node].accept:
            return True
    return False

# if exist the node into the tree
def exist_node(tree, state):
    for node in tree.state:
        if Counter(node.name) == Counter(state):
            return False
    return True

def subset(automata, expresion):
    dfa = Automata(automata.expresion)
    current_node = [0]
    data_symbol = get_symbol(automata)

    #subset method
    e_lock = ecerradura(automata, current_node)
    new_node = State(e_lock, len(dfa.state))
    # create node (s_o) 
    dfa.state.append(new_node)
    # verificate existing node
    if accept_node(automata, new_node.name):
        new_node.accept = True
    
    for node in dfa.state:
        # search for symbol
        for symbol in data_symbol:
            epsilon = []
            val = []
            for i in node.name:
                for transition in automata.state[i].transition:
                    if transition.symbol == symbol:
                        # add the value
                        val.append(transition.id)
            # epsilon lock of movemnt
            epsilon = ecerradura(automata, val)
            if exist_node(dfa, epsilon) and epsilon != []:
                new_node_current = State(epsilon, len(dfa.state))
                dfa.state.append(new_node_current)
                if accept_node(automata, epsilon):
                    new_node_current.accept = True
                node.transition.append(Handler(symbol, dfa.state[-1].id))
            elif epsilon != []:
                add = add_tree(dfa, epsilon)
                if add:
                    node.transition.append(Handler(symbol, add.id))
                else:
                    print('There is no node with' + epsilon + 'de id')
    return dfa

def add_tree(automata, id):
    for node in automata.state:
        if Counter(node.name) == Counter(id):
            return node
    return False


