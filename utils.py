'''
    reference to grahipviz https://graphviz.readthedocs.io/en/stable/manual.html
'''
from graphviz import Digraph
from Thompson.evaluador_expresion import list_to_string, EPSILON
from DFA_Direct.dfa_direct import OPERATORS
from DFA.dfa import get_symbol

def graphic(exp, data, name):
    dot = Digraph(name='Automata')
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='doublecircle')

    for i in range(len(data)):
        dot.node(str(data[i][1]))
        
    dot.attr('node', shape='circle')

    for i in range(len(exp)):
        dot.edge(str(exp[i][0]), str(exp[i][2]), label= str(exp[i][1]))
    
    dot.render('Graph/'+name+'.gv', view=True)

def save_txt(data, state_info, expresion, name):
    data_save = open('Text/'+ name + '.txt', 'w+', encoding="utf-8")

    state = []
    symbol = []
    for i in range(len(data)):
        if data[i][0] not in state:
            state.append(data[i][0])

        if data[i][2] not in state:
            state.append(data[i][2])
                
        if data[i][1] not in symbol:
            symbol.append(data[i][1])
    
    exp = list_to_string(expresion)
    data_save.write('Automata Evaluada: ' + exp + '\n')
    data_save.write('='*len(data) + '\n' + 'Estados: ' + str(state) + '\n')
    data_save.write('Simbolos: ' + str(symbol) + '\n')

    for i in range(len(state_info)):
        information = state_info[i][0]
        data_save.write('='*len(data) + '\n' +'Estado Inicial: ' + str(information) + '\n')

    for i in range(len(state_info)):
        information = state_info[i][1]
        data_save.write('='*len(data) + '\n' +'Estado Aceptacion: ' + str(information) + '\n')
    
    data_save.write('='*len(data) + '\n' +'Transiciones: ' + str(data) + '\n')

def error(expresion):
    # si encuentra un parentesis abierto
    if '(' in expresion:
        # si se cierra el parentesis, no hay errores retorna True
        if (expresion.count('(') == expresion.count(')')):
            return True
        else:
            return False
    else:
        return True

def verificate(char):
    for x in char:
        if x.isalpha():
            return True
        elif x == EPSILON:
            return True
        elif x.isnumeric():
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

def error(expresion):
    # si encuentra un parentesis abierto
    if '(' in expresion:
        # si se cierra el parentesis, no hay errores retorna True
        if (expresion.count('(') == expresion.count(')')):
            return True
        else:
            return False
    else:
        return True

def graphic_tree(automata, name):
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

def save_txt_tree(automata, name):
    data_save = open('Text/'+ name + '.txt', 'w+', encoding="utf-8")
    
    data_symbol = get_symbol(automata)

    data_save.write('Automata Evaluada: ' + str(automata.expresion) + '\n')
    data_save.write('Simbolos del la expresion: ')
    # print('Automata Evaluada: %s ' % str(automata.expresion))

    # reccoremos los simbolos que se encuentren
    for symbol in data_symbol:
        data_save.write(symbol + ' ')
    data_save.write('\n')

    # recorremos los estados que se tienen
    for state in automata.state:
        data_save.write('\n')
        if(state.id == 0):
            data_save.write('Nodo Inicial: ' + str(state.id) + '\n')
        if(state.accept):
            data_save.write('')
        data_save.write('Aceptacion: ' + str(state.id) + '\n')
        #print('Aceptación: %s' % str(state.id))

        for transition in state.transition:
            data = f"{transition.symbol} --> {transition.id}\n"
            data_save.write(data)
            # if transition.symbol == EPSILON:
                # data_save.write(str('\u03B5') + '-->' + str(transition.id))
            #print(data)
            
    data_save.close()