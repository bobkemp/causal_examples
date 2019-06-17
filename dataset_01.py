import networkx as nx
from random import random, seed, uniform, gauss


g = nx.DiGraph()

g.add_edges_from([
    ("B", "X"),
    ("B", "A"),
    ("B", "Y"),
    ("X", "A"),
    ("X", "Y"),
])

draw_fn = nx.draw_planar

B_A_coeff = 2
B_X_coeff = 3
B_Y_coeff = -1
X_A_coeff = 1.25
X_Y_coeff = 1


def B_value():
    return 5 * uniform(-1, 1)

def X_value(b):
    return B_X_coeff * b + gauss(1, 2)

def A_value(b, x):
    return B_A_coeff * b + X_A_coeff * x + gauss(3, 0.25)

def Y_value(b, x):
    return B_Y_coeff * b + X_Y_coeff * x + gauss(9, 4)

def observation():
    b = B_value()
    x = X_value(b)
    a = A_value(b, x)
    y = Y_value(b, x)
    
    return (a, b, x, y)

