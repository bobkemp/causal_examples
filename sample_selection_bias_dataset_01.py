import networkx as nx
from random import random, seed, uniform, gauss


g = nx.DiGraph()

g.add_edges_from([
    ("X",  "Y"),
    ("W1", "S"),
    ("W1", "W2"),
    ("W1", "X"),
    ("W2", "X"),
    ("Z",  "W2"),
    ("Z",  "Y"),
])

draw_fn = nx.draw_planar

X_Y_coeff = 1
W1_S_coeff = 2.3
W1_W2_coeff = 4
W1_X_coeff = 3
W2_X_coeff = 2
Z_W2_coeff = 3
B_Y_coeff = -1
Z_Y_coeff = 1.25


def W1_value():
    return 5 * uniform(-1, 1)

def Z_value():
    return 3 * uniform(-1, 1)

def W2_value(w1, z):
    return W1_W2_coeff * w1 + Z_W2_coeff * z + gauss(1, 2)

def X_value(w1, w2):
    return W1_X_coeff * w1 + W2_X_coeff * w2 + gauss(3, 0.25)

def Y_value(x, z):
    return X_Y_coeff * x + Z_Y_coeff * z + gauss(9, 4)

def S_value(w1):
    return 1 if w1 > 0 else 0

def observation():
    w1 = W1_value()
    z = Z_value()
    w2 = W2_value(w1, z)
    x = X_value(w1, w2)
    y = Y_value(x, z)
    s = S_value(w1)
    
    return (s, w1, w2, x, y, z)

