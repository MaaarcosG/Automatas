#from Thompson.prueba import Prueba

from Thompson.operations import *
from utils import *
exp = "a|b"

data = regex(exp)
automata = create_automata(data, exp)
graphic(automata, 'Thompson')
save_txt(automata, 'Thompson')