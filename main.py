# some functions
from Thompson.operations import regex, create_automata
from DFA.dfa import subset
from utils import graphic, save_txt, read_file, computarizable
from DFA.simulate import simulate
from DFA_Direct.dfa_direct import sintetic_tree, OPERATORS
from collections import OrderedDict
# data epsilon
EPSILON = "ε"

while True:
    mensaje = ('Ingrese la expresión regular: ')
    menu = input("\n1. Contruccion de Thompson \n2. Contruccion de Subconjuntos \n3. Construcción de AFD dada una expresión regular\n4. ¿Desea salir? \n Escoga una opcion: ")
    if menu == '1':
        print('-' * len(mensaje))
        # expresion = '('+EPSILON+'.a|'+EPSILON+'.b)*.a.b.b'
        expresion = input(mensaje)
        expresion_computabii = computarizable(expresion)
        print('La expresion computarizada es: %s' % expresion_computabii)
        data = regex(expresion_computabii)
        automata = create_automata(data, expresion_computabii)

        # creamos el grafo junto a su txt
        print('CREANDO EL GRAFO....')
        print('CREANDO EL TXT....')
        graphic(automata, 'Thompson')
        # save_txt(automata, 'Thompson')
        
        ## DEBERIA HACER LA SIMULACION
        expresion_2 = input('Ingrese la expresion que quiere probar: ')
        print('EVALUACIÓN NFA')
        evaluación = simulate(automata, expresion_2)
        print(evaluación)
    
    elif menu == '2':
        print('-' * len(mensaje))
        expresion = input(mensaje)
        expresion_computabii = computarizable(expresion)
        print('La expresion computarizada es: %s' % expresion_computabii)

        data = regex(expresion_computabii)
        automata = create_automata(data, expresion_computabii)

        # DFA
        dfa = subset(automata, expresion)
        print('CREANDO EL GRAFO....')
        print('CREANDO EL TXT....')
        graphic(dfa, 'DFA')
        #save_txt(dfa, 'DFA')

        ## DEBERIA HACER LA SIMULACION
        expresion_2 = input('Ingrese la expresion que quiere probar: ')
        print('EVALUACIÓN DE SUBCONJUNTOS')
        evaluación = simulate(dfa, expresion_2)
        print(evaluación)
    
    elif menu == '3':
        print('-' * len(mensaje))
        # expresion = '((a|b)*.((a|(b.b))*.'+EPSILON+'))'
        expresion = input(mensaje)
        expresion_computabii = computarizable(expresion)
        print('La expresion computarizada es: %s' % expresion_computabii)

        data = regex(expresion_computabii)
        direct_dfa = sintetic_tree(data, expresion)

        # construcción directa
        print('CREANDO EL GRAFO....')
        print('CREANDO EL TXT....')
        graphic(direct_dfa, 'DFA_Direct')
        save_txt(direct_dfa, 'DFA_Direct')

        ## DEBERIA HACER LA SIMULACION
        expresion_2 = input('Ingrese la expresion que quiere probar: ')
        print('METODO DIRECTO')
        evaluación = simulate(direct_dfa, expresion_2)
        print(evaluación)

    elif menu == '4':
        break

