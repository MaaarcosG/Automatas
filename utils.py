# graphic
from graphviz import Digraph

# global variables
OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
SPECIAL = ['*', '+', '?']
EPSILON = "ε"

def graphic(automata, name):
    dot = Digraph(name='Automata')
    dot.attr(rankdir = 'LR')
    for state in automata.state:
        if state.accept:
            dot.node(str(state.id), str(state.id), shape='doublecircle')
        else:
            dot.node(str(state.id), str(state.id))
        for transition in state.transition:
            dot.edge(str(state.id), str(transition.id), transition.symbol)
    dot.render('Graph/'+name+'.gv', view=True)

def save_txt(automata, name):
    data_save = open('Text/'+ name + '.txt', 'w')
    data_symbol = []
    for symbol in automata.expresion:
        if (symbol not in OPERATORS) and (symbol not in data_symbol) and (symbol != EPSILON):
            data_symbol.append(symbol)
    data_save.write('Automata Evaluada: ' + str(automata.expresion) + '\n')
    data_save.write('Simbolos del la expresión: ')
    for symbol in data_symbol:
        data_save.write(symbol + ' ')
    data_save.write('\n')
    for state in automata.state:
        data_save.write('\n')
        if(state.id == 0):
            data_save.write('INICIAL \n')
        if(state.accept):
            data_save.write('-> ')
        data_save.write('Aceptación: ' + str(state.id) + '\n')
        for transition in state.transition:
            data_save.write('Con: ' + str(transition.symbol) + '--> ' + str(transition.id) + '\n')
    data_save.close()
        


