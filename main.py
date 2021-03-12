#from Thompson.prueba import Prueba

# data epsilon
EPSILON = "ε"

# some functions
from Thompson.operations import regex, create_automata
from DFA.dfa import subset
from utils import graphic, save_txt
from DFA.simulate import simulate
from DFA_Direct.dfa_direct import sintetic_tree


#exp = '(a|'+EPSILON+').b.(a+).c?'
exp = '(a*|b*).c'

print(exp)

data = regex(exp)
automata = create_automata(data, exp)

'''
graphic(automata, 'Thompson')
save_txt(automata, 'Thompson')

dfa = subset(automata, exp)
graphic(dfa, 'DFA')
save_txt(dfa, 'DFA')
'''

direct_dfa = sintetic_tree(data, exp)
graphic(direct_dfa, 'DFA_Direct')
save_txt(direct_dfa, 'DFA_Direct')

'''
while True:
    expresion = input('Ingrese una expresión para evaluar: ')
    print('Evaluación de AFN con la expresion %s' % expresion)
    print(simulate(automata, expresion))

    continuar = input('¿Desea continuar? S/N ')
    if (continuar == 'N'):
        break
'''