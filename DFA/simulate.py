from DFA.dfa import ecerradura
from Thompson.nfa import Automata, State, Handler

EPSILON = "ε"

def simulate(automata, expresion):
    if expresion == ' ':
        expresion = EPSILON
    current_node = [0]
    current_node = ecerradura(automata, current_node)
    i = 0
    while True:
        value = []
        '''
        print("Simbolos: %s " % expresion[i])
        print("Estados: %s " % current_node)
        '''
        for node in current_node:
            for transitions in automata.state[node].transition:
                # si el simbolo se encuentra en la expresion y no en los evaluados, se agrega a la lista
                if (transitions.symbol == expresion[i]) and (transitions.id not in value):
                    value.append(transitions.id)
        i += 1
        # tomamos de la lista la nueva cerradura
        value = ecerradura(automata, value)
        
        # si no esta en la cerrado, y la expresion solo tiene epsilon, terminamos el ciclo
        if (not value) and (expresion == EPSILON):
            break
        
        # si el contador se acaba terminamos el prcesos copiamos los datos a la lista
        current_node = value.copy()
        if i > len(expresion)-1:
            break
    # recorremos la lista, para ver si son aceptados o no
    for node in current_node:
        if automata.state[node].accept == True:
            return 'Si'
    return 'No'