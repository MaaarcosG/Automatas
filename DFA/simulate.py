from DFA.dfa import ecerradura

EPSILON = "ε"

def simulate(automata, expresion):
    # if empty the expresion add EPSILON
    if (expresion == " "):
        expresion = EPSILON

    # take the function ecerradura current node
    node = ecerradura(automata, [0])
    # print(node)
    # counter
    i = 0
    while True:
        value = []
        for j in node:
            for transition in (automata.state[j].transition):
                # if found and no have move
                # print(transition.id)
                if (transition.symbol == expresion[i]) and (transition.id not in value):
                    value.append(transition.id)
        i += 1
        value = ecerradura(automata, value)
        # print(value)
        # finish when no have more move
        if not value and (expresion==EPSILON):
            break
        node = value.copy()
        # print(node)
        if i > len(expresion)-1:
            break
    for k in node:
        # accept the expresion return YES
        if automata.state[k].accept:
            acceptation = 'YES'
            print(acceptation)
            return True
        else:
            acceptation = 'NO'
            print(acceptation)
            return False
