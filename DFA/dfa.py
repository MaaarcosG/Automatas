'''
    Convert Nodeterministic finite automatan (NFA) to Deterministic finite automatan (DFA)
'''

# to create the automata
from Thompson.nfa import Automata

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
SPECIAL = ['*', '+', '?']
EPSILON = "ε"


