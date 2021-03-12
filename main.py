# some functions
from Thompson.operations import regex, create_automata
from DFA.dfa import subset
from utils import graphic, save_txt, read_file
from DFA.simulate import simulate
from DFA_Direct.dfa_direct import sintetic_tree
from collections import OrderedDict
# data epsilon
EPSILON = "ε"

while True:
    mensaje = ('Ingrese la expresión regular: ')
    menu = input("\n1. Contruccion de Thompson \n2. Contruccion de Subconjuntos \n3. Construcción de AFD dada una expresión regular\n4. ¿Desea salir? \n Escoga una opcion: ")
    if menu == '1':
        print('-' * len(mensaje))
        expresion = input(mensaje)
        print('La expresion ingresada fue: %s' % expresion)
        data = regex(expresion)
        automata = create_automata(data, expresion)
        # creamos el grafo junto a su txt
        print('CREANDO EL GRAFO....')
        print('CREANDO EL TXT....')
        graphic(automata, 'Thompson')
        save_txt(automata, 'Thompson')

        ## DEBERIA HACER LA SIMULACION
    
    elif menu == '2':
        print('-' * len(mensaje))
        expresion = input(mensaje)
        print('La expresion ingresada fue: %s' % expresion)
        data = regex(expresion)
        automata = create_automata(data, expresion)
        # DFA
        dfa = subset(automata, expresion)
        print('CREANDO EL GRAFO....')
        print('CREANDO EL TXT....')
        graphic(dfa, 'DFA')
        save_txt(dfa, 'DFA')
    
    elif menu == '3':
        print('-' * len(mensaje))
        expresion = input(mensaje)
        print('La expresion ingresada fue: %s' % expresion)
        data = regex(expresion)
        # construcción directa
        direct_dfa = sintetic_tree(data, expresion)
        print('CREANDO EL GRAFO....')
        print('CREANDO EL TXT....')
        graphic(direct_dfa, 'DFA_Direct')
        save_txt(direct_dfa, 'DFA_Direct')

    elif menu == '4':
        break

