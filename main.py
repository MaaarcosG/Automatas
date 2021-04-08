from utils import graphic, save_txt, graphic_tree, save_txt_tree, computarizable, error
from Thompson.evaluador_expresion import change_data, regex, regex_tree
from Thompson.operations import get_operation, delete_parentesis
from DFA.dfa import subset
from DFA.simulate import simulate_dfa, simulate_nfa
from DFA_Direct.dfa_direct import sintetic_tree, OPERATORS

while True:
    mensaje = ('Ingrese la expresión regular: ')
    menu = input("\n1. Contruccion de Thompson \n2. Contruccion de Subconjuntos \n3. Construcción de AFD dada una expresión regular\n4. ¿Desea salir? \n Escoga una opcion: ")
    if menu == '1':
        expresion = regex(change_data(input('Ingrese una expresion: ')))
        # eliminamos los parentesis para la creacion
        delete_parentesis(expresion)
        exp, data = get_operation(expresion)
        graphic(exp, data, 'Thompson')
        save_txt(exp, data, expresion, 'Thompson')
        # contador para la simulacion
        count = True
        while count:
            expresion_2 = input('Ingrese la expresion que quiere probar: ')
            print('Simulacion de NFA %s pertenece al lenguaje' % simulate_nfa(expresion_2, exp, data))
            op = input('Desea evaluar otra S/N: ')
            if op == 'N':
                count = False

    elif menu == '2':
        expresion = regex(change_data(input('Ingrese una expresion: ')))
        # eliminamos los parentesis para la creacion
        delete_parentesis(expresion)
        exp, data = get_operation(expresion)
        automata, new_state = subset(exp, data)
        # graficamos
        graphic(automata, new_state, 'DFA')
        # guardamos la informacion en un txt
        save_txt(automata, new_state, expresion, 'DFA')
        # contador para la simulacion
        count = True
        while count:
            expresion_2 = input('Ingrese la expresion que quiere probar: ')
            print('Simulacion de DFA %s pertecene al lenguaje' % simulate_dfa(expresion_2, automata, new_state))
            op = input('Desea evaluar otra S/N: ')
            if op == 'N':
                count = False

    elif menu == '3':
        print('-' * len(mensaje))
        # expresion = '((a|b)*.((a|(b.b))*.'+EPSILON+'))'
        expresion = input(mensaje)
        expresion_computabii = computarizable(expresion)
        print('La expresion computarizada es: %s' % expresion_computabii)

        if error(expresion_computabii):
            data = regex_tree(expresion_computabii)
            direct_dfa = sintetic_tree(data, expresion)

            # construcción directa
            graphic_tree(direct_dfa, 'DFA_Direct')
            save_txt_tree(direct_dfa, 'DFA_Direct')
        else:
            error_msg = ('La expresion %s tiene errores, por parentesis' % expresion_computabii)
            print('-'*len(error_msg))
            print(error_msg)

    elif menu == '4':
        break
    else:
        print('Opcion no disponible')