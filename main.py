#from Thompson.prueba import Prueba

from Thompson.operations import *

exp = "(a*|b*).c"

data = regex(exp)
print(data)

automata = create_automata(data, exp)
print(automata)

graphic(automata, 'Thompson')