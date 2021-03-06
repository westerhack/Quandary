from constants import constants
from node import node, getiter
from knowndict import knowndict
n = node(constants())
with open('qfiles/testcode.qq') as f:
    gen = getiter(n.consts, f.read())
known = knowndict(n.consts)
print('----')
print(n.evalnode(gen, known), known)
print('----\n')
if __debug__ and '$dnd' not in known:
    print(known, end = '\n--\n')
    print(repr(known))