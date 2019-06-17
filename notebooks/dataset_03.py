import networkx as nx
from random import random, seed, uniform, gauss


g = nx.DiGraph()

g.add_edges_from([
    ("Z1", "X"),
    ("Z1", "Z3"),
    ("Z2", "Z3"),
    ("Z2", "Y"),
    ("Z3", "X"),
    ("Z3", "Y"),
    ("X", "W"),
    ("W", "Y"),
])

draw_fn = nx.draw_kamada_kawai

Z2_Y_coeff = 2
Z2_Z3_coeff = 3
Z3_Y_coeff = 7
Z3_X_coeff = 1
Z1_Z3_coeff = 1.25
Z1_X_coeff = -2
X_W_coeff = 1.5
W_Y_coeff = 1


def Z1_value():
    return 5 * uniform(-1, 1)

def Z2_value():
    return 3 * uniform(-1, 1)

def Z3_value(z1, z2):
    return Z1_Z3_coeff * z1 + Z2_Z3_coeff * z2 + gauss(3, 0.25)

def W_value(x):
    return X_W_coeff * x + gauss(1, 0.75)

def X_value(z1, z3):
    return Z1_X_coeff * z1 + Z3_X_coeff * z3 + gauss(-1, 2)

def Y_value(w, z2, z3):
    return W_Y_coeff * w + Z2_Y_coeff * z2 + Z3_Y_coeff * z3 + gauss(9, 4)

def observation():
    z1 = Z1_value()
    z2 = Z2_value()
    z3 = Z3_value(z1, z2)
    x = X_value(z1, z3)
    w = W_value(x)
    y = Y_value(w, z2, z3)
    
    return (w, x, y, z1, z2, z3)

