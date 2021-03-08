#from Thompson.prueba import Prueba

from Thompson.tree import *
from Thompson.nfa import *

exp = "(a*|b*).c"

data = regex(exp)
print(data)

automata = automata(data, exp)
print(automata)
