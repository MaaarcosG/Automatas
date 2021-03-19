# some functions
from Thompson.operations import regex, create_automata
from DFA.dfa import subset
from utils import graphic, save_txt, computarizable, error
from DFA.simulate import simulate, alphabet
from DFA_Direct.dfa_direct import sintetic_tree, OPERATORS
from collections import OrderedDict
# data epsilon
EPSILON = "ε"

while True:
    mensaje = ('Ingrese la expresión regular: ')
    menu = input("\n1. Contruccion de Thompson y Contruccion de Subconjuntos \n2. Construcción de AFD dada una expresión regular\n3. ¿Desea salir? \n Escoga una opcion: ")
    if menu == '1':
        print('-' * len(mensaje))
        # expresion = '('+EPSILON+'.a|'+EPSILON+'.b)*.a.b.b'
        expresion = input(mensaje)
        expresion_computabii = computarizable(expresion)
        print('La expresion computarizada es: %s' % expresion_computabii)

        if error(expresion_computabii):
            # información para crear el automata despues de la conversion
            data = regex(expresion_computabii)
            automata = create_automata(data, expresion_computabii)
            
            alphabeto = alphabet(expresion_computabii)

            # Implementación de thompson
            graphic(automata, 'Thompson')
            save_txt(automata, 'Thompson')

            # Implementación de Subconjuntos
            dfa = subset(automata, expresion_computabii)
            graphic(dfa, 'DFA')
            save_txt(dfa, 'DFA')

            print('CREANDO LOS GRAFO DE LAS IMPLEMENTACIONES....')
            print('CREANDO LOS ARCHIVOS TXT DE LAS TRANSICIONES....')
        
            count = True
            while count:
                expresion_2 = input('Ingrese la expresion que quiere probar: ')
                evaluacion_nfa = simulate(automata, expresion_2, alphabeto)
                evaluacion_dfa = simulate(dfa, expresion_2, alphabeto)
                print('Simulacion de NFA: %s' % evaluacion_nfa)
                print('Simulacion de DFA: %s' % evaluacion_dfa)
                op = input('Desea evaluar otra S/N: ')
                if op == 'N':
                    count = False
        else:
            print('La expresion %s tiene errores, por parentesis' % expresion_computabii)

    elif menu == '2':
        print('-' * len(mensaje))
        # expresion = '((a|b)*.((a|(b.b))*.'+EPSILON+'))'
        expresion = input(mensaje)
        expresion_computabii = computarizable(expresion)
        print('La expresion computarizada es: %s' % expresion_computabii)

        if error(expresion_computabii):
            data = regex(expresion_computabii)
            direct_dfa = sintetic_tree(data, expresion)

            # construcción directa
            print('CREANDO EL GRAFO....')
            print('CREANDO EL TXT....')
            graphic(direct_dfa, 'DFA_Direct')
            save_txt(direct_dfa, 'DFA_Direct')
        else:
            error_msg = ('La expresion %s tiene errores, por parentesis' % expresion_computabii)
            print('-'*len(error_msg))
            print(error_msg)

    elif menu == '3':
        break
    else:
        print('Opcion no disponible')

