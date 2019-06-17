import networkx as nx
from random import random, seed, uniform, gauss


g = nx.DiGraph()

g.add_edges_from([
    ("T1",  "X"),
    ("W1",  "S"),
    ("W1",  "T1"),
    ("W2",  "S"),
    ("W2",  "Y"),
    ("W3",  "Y"),
    ("X",   "W3"),
    ("Z1",  "W1"),
    ("Z1",  "Z3"),
    ("Z2",  "W2"),
    ("Z2",  "Z3"),
    ("Z3",  "X"),
    ("Z3",  "Y"),
])

draw_fn = nx.draw_circular

T1_X_coeff = 1
W1_S_coeff = 3.2
W1_T1_coeff = 2.3
W2_S_coeff = -1.2
W2_Y_coeff = 4
W3_Y_coeff = 3
X_W3_coeff = -2
Z1_W1_coeff = 3
Z1_Z3_coeff = -1
Z2_W2_coeff = 2.2
Z2_Z3_coeff = 7
Z3_X_coeff = -1.5
Z3_Y_coeff = 1.75


def Z1_value():
    return 5 * uniform(-1, 1)

def Z2_value():
    return 3 * uniform(-1, 1)

def W1_value(z1):
    return Z1_W1_coeff * z1 + gauss(1, 2)

def T1_value(w1):
    return W1_T1_coeff * w1 + gauss(1, 2)

def X_value(t1, z3):
    return T1_X_coeff * t1 + Z3_X_coeff * z3 + gauss(3, 0.25)

def Z3_value(z1, z2):
    return Z1_Z3_coeff * z1 + Z2_Z3_coeff * z2 + gauss(9, 4)

def W2_value(z2):
    return Z2_W2_coeff * z2 + gauss(4, 9)

def W3_value(x):
    return X_W3_coeff * x + gauss(0, 1)

def Y_value(w2, w3, z3):
    return W2_Y_coeff * w2 + W3_Y_coeff * w3 + Z3_Y_coeff * z3 + gauss(-2, 1)

def S_value(w1, w2):
    return 1 if w1 > 1 and w2 > 4 else 0

def observation():
    z1 = Z1_value()
    z2 = Z2_value()
    z3 = Z3_value(z1, z2)
    w1 = W1_value(z1)
    w2 = W2_value(z2)
    t1 = T1_value(w1)
    x  = X_value(t1, z3)
    w3 = W3_value(x)
    y  = Y_value(w2, w3, z3)
    s  = S_value(w1, w2)
    
    return (s, t1, w1, w2, w3, x, y, z1, z2, z3)
