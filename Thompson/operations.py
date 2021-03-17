'''
 Reference https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b
'''
from Thompson.nfa import Automata
from Thompson.nfa import Handler
from Thompson.nfa import State
from Thompson.tree import Tree

# global variables
OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
SPECIAL = ['*', '+', '?']
EPSILON = "ε"

def regex(expresion):
    values = []
    operation = []
    # counter
    i = 0
    while (i < len(expresion)):
        # there is space
        if (expresion[i] == ' '):
            i += 1
            continue
        # there is open parentesis
        elif (expresion[i] == "("):
            operation.append(expresion[i])
        
        elif (expresion[i] not in OPERATORS):
            val = ""
            while (i < len(expresion)) and expresion[i] not in OPERATORS:
                val = str(val) + expresion[i]
                i -= -1
            # take the class of tree
            tree = Tree()
            tree.data = val
            # append to list data of the tree
            values.append(tree)
            i -= 1
        # there is close parentesis
        elif expresion[i] == ")":
            while len(operation) != 0 and operation[-1] != "(":
                val2 = values.pop()
                val1 = values.pop()
                op = operation.pop()
                # take the class of tree
                tree = Tree()
                tree.data = op
                tree.left = val1
                tree.right = val2
                # add the data to list
                values.append(tree)
            operation.pop()

        # expresion[i] == '('
        else:
            if (expresion[i] in SPECIAL):
                op = expresion[i]
                val = values.pop()
                # take the class of tree
                tree = Tree()
                tree.data = op
                tree.left = val
                tree.right = None
                # add the data to list
                values.append(tree)
            else:
                while (len(operation) != 0  and operation[-1] != '('):
                    op = operation.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    # take the class of tree
                    tree = Tree()
                    tree.data = op
                    tree.left = val1
                    tree.right = val2
                    # add the data to list
                    values.append(tree)
                operation.append(expresion[i])
        
        i -= -1
    
    # if no empty the list 
    while(len(operation) != 0):
        val2 = values.pop()
        val1 = values.pop()
        op = operation.pop()
        # take the class of tree
        tree = Tree()
        tree.data = op
        tree.left = val1
        tree.right = val2
        # add the data to list
        values.append(tree)
        if (len(values) == 1):
            return values[-1]

    return values[-1]

def create_automata(tree, expresion):
    data = Automata(expresion)
    _, b = transition_handler(tree, data)
    b.accept = True
    return data

def transition_handler(tree, automata):
    a = 0
    b = 0

    # we walk the tree looking for the symbols
    if tree.data in OPERATORS:
        if(tree.data == '.'):
            # concatenation
            a, b = concatenation(tree, automata)
        elif(tree.data == '|'):
            # symbol_or
            a, b = symbol_or(tree, automata)
        elif(tree.data == '*'):
            # kleene
            a, b = kleene(tree, automata)
        elif(tree.data == '+'):
            # union
            a, b = union(tree, automata)
        elif(tree.data == '?'):
            # symbol_question
            a, b = symbol_question(tree, automata)
    else:
        # unique_symbol
        a, b = unique_symbol(tree, automata)
    return a, b

# represent . 
def concatenation(tree, automata):
    # print(tree.left.data)
    if tree.left.data in OPERATORS:
        a, b = transition_handler(tree.left, automata)
    else:
        a, b = unique_symbol(tree.left, automata)
    
    if tree.right.data in OPERATORS:
        a1, b1 = transition_handler(tree.right, automata)
    else:
        a1, b1 = unique_symbol(tree.right, automata)

    b.transition.append(Handler(EPSILON, a1.name))
    # print(b)

    return a, b1

# return a+ = a*a
# return a+ = aa* a.a**
def union(tree, automata):
    # print(tree.left.data) 
    if tree.left.data in OPERATORS:
        a, b = transition_handler(tree.left, automata)
    else:
        a, b = unique_symbol(tree.left, automata)

    value = Tree()
    value.data = '*'
    value.left = tree.left

    a1, b1 = kleene(value, automata)
    b.transition.append(Handler(EPSILON, a1.name))
    print(b1)

    return a, b1

def symbol_or(tree, automata):
    start = State(len(automata.state), len(automata.state))
    automata.state.append(start)
    # print(tree.left.data)
    if tree.left.data in OPERATORS:
        a, b = transition_handler(tree.left, automata)
    else:
        a, b = unique_symbol(tree.left, automata)

    if tree.right.data in OPERATORS:
        a1, b1 = transition_handler(tree.right, automata)
    else:
        a1, b1 = unique_symbol(tree.right, automata)
    
    end = State(len(automata.state), len(automata.state))
    automata.state.append(end)

    start.transition.append(Handler(EPSILON, a.name))
    start.transition.append(Handler(EPSILON, a1.name))
    b.transition.append(Handler(EPSILON, end.name))
    b1.transition.append(Handler(EPSILON, end.name))

    return start, end

# return a* = a+ | EPSILON
def kleene(tree, automata):
    start = State(len(automata.state), len(automata.state))
    automata.state.append(start)
    # print(automata.state)

    if tree.left.data in OPERATORS:
        a, b = transition_handler(tree.left, automata)
    else:
        a, b = unique_symbol(tree.left, automata)
    
    end = State(len(automata.state), len(automata.state))
    automata.state.append(end)
    print('Start %s ' % start)
    print('End %s ' % end)

    start.transition.append(Handler(EPSILON, a.name))
    start.transition.append(Handler(EPSILON, end.name))
    b.transition.append(Handler(EPSILON, a.name))
    b.transition.append(Handler(EPSILON, end.name))

    return start, end

# return a? = a | EPSILON
def symbol_question(tree, automata):
    value = Tree()
    value_2 = Tree()

    value_2.data = EPSILON
    value.data = '|'
    value.left = tree.left
    value.right = value_2

    a, b = symbol_or(value, automata)

    return a, b

def unique_symbol(tree, automata):
    symbol = tree.data
    first = State(len(automata.state), len(automata.state))
    automata.state.append(first)
    second = State(len(automata.state), len(automata.state))
    automata.state.append(second)
    first.transition.append(Handler(symbol, second.id))
    
    return first, second