'''
 Reference https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b
'''

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
EPSILON = "ε"

def transition_handler(tree, automata):
    start = 0
    finish = 0

    # we walk the tree looking for the symbols
    if tree.data in OPERATORS:
        if(tree.data == '.'):
            # concatenation
            pass
        elif(tree.data == '+'):
            # union
            pass
        elif(tree.data == '|'):
            # symbol_or
            pass
        elif(tree.data == '*'):
            # kleene
            pass
        elif(tree.data == '?'):
            # symbol_question
            pass
    else:
        # unique_symbol
        pass
    return start, finish

def concatenation(tree, automata):
    pass

def union(tree, automata):
    pass

def symbol_or(tree, automata):
    pass

def kleene(tree, automata):
    pass

def symbol_question(tree, automata):
    pass

def unique_symbol(tree, automata):
    pass

