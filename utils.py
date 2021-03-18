'''
    reference to grahipviz https://graphviz.readthedocs.io/en/stable/manual.html
'''
from graphviz import Digraph
from DFA.dfa import get_symbol, EPSILON, OPERATORS

def graphic(automata, name):
    dot = Digraph(name='Automata')
    dot.attr(rankdir = 'LR')
    
    for state in automata.state:
        # print(state.id)
        if state.accept:
            dot.node(str(state.id), str(state.id), shape='doublecircle')
        else:
            dot.node(str(state.id), str(state.id))
        for transition in state.transition:
            # print(transition.id)
            dot.edge(str(state.id), str(transition.id), transition.symbol)
    dot.render('Graph/'+name+'.gv', view=True)

def save_txt(automata, name):
    data_save = open('Text/'+ name + '.txt', 'w+')

    data_symbol = get_symbol(automata)

    # data_save.write('Automata Evaluada: ' + str(automata.expresion) + '\n')
    # data_save.write('Simbolos del la expresion: ')
    print('Automata Evaluada: %s ' % str(automata.expresion))

    for symbol in data_symbol:
        data_save.write(symbol + ' ')
    data_save.write('\n')

    for state in automata.state:
        data_save.write('\n')
        if(state.id == 0):
            data_save.write('INICIAL \n')
        if(state.accept):
            data_save.write('')
        # data_save.write('Aceptacion: ' + str(state.id) + '\n')
        print('Aceptación: %s' % str(state.id))

        for transition in state.transition:
            # data_save.write(str(transition.symbol) + '--> ' + str(transition.id) + '\n')
            data = f"{transition.symbol} --> {transition.id}\n"
            # if transition.symbol == EPSILON:
                # data_save.write(str('\u03B5') + '-->' + str(transition.id))
            print(data)
    data_save.close()
        
def read_file(path='expressions'):
    file = open(path+'.txt', 'r')
    line = file.readlines()
    file.close()
    return line

def verificate(char):
    if char.isalpha():
        return True
    elif char == EPSILON:
        return True
    elif char.isnumeric():
        return True
    else:
        return False

def computarizable(expresion):
    exp = ''
    for i in range(0, len(expresion)):
        if i == 0:
            exp = exp + expresion[i]
        else:
            if verificate(expresion[i-1]) and verificate(expresion[i]):
                exp = exp + '.' + expresion[i]
            elif verificate(expresion[i-1]) and verificate(expresion) == '(':
                exp = exp + '.' + expresion[i]
            elif verificate(expresion[i]) and verificate(expresion[i-1]) == ')':
                exp = exp + '.' + expresion[i]
            elif expresion[i-1] == '*' and verificate(expresion[i]):
                exp = exp + '.' + expresion[i]
            elif expresion[i-1] == '*' and expresion[i] == '(':
                exp = exp + '.' + expresion[i]
            elif expresion[i-1] == ')' and expresion[i] == '(':
                exp = exp + '.' + expresion[i]
            elif expresion == '?':
                exp = exp + '?'
            elif expresion[i-1] == ')' and (expresion[i] not in OPERATORS):
                exp = exp + '.' + expresion[i]
            elif expresion[i-1] == EPSILON:
                exp = exp + EPSILON + expresion[i]
            else:
                exp = exp + expresion[i]
    return exp  
