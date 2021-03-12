#from Thompson.prueba import Prueba

# data epsilon
EPSILON = "ε"

# some functions
from Thompson.operations import regex, create_automata
from DFA.dfa import subset
from utils import graphic, save_txt

#exp = '(a|'+EPSILON+').b.(a+).c?'
exp = '(a*|b*).c'
print(exp)

data = regex(exp)
automata = create_automata(data, exp)

graphic(automata, 'Thompson')
save_txt(automata, 'Thompson')

dfa = subset(automata, exp)
graphic(dfa, 'DFA')
save_txt(dfa, 'DFA')