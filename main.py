#from Thompson.prueba import Prueba

from Thompson.operations import *
from DFA.dfa import *
from utils import *

exp = '(a*|b*).c'

data = regex(exp)
automata = create_automata(data, exp)

graphic(automata, 'Thompson')
save_txt(automata, 'Thompson')

dfa = subset(automata, exp)
graphic(dfa, 'DFA')
save_txt(dfa, 'DFA')