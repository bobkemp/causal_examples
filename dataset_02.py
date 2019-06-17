import networkx as nx
from random import random, seed, uniform, gauss


g = nx.DiGraph()

g.add_edges_from([
    ("X", "D"),
    ("B", "X"),
    ("B", "D"),
    ("D", "Y"),
    ("X", "A"),
    ("A", "C"),
    ("A", "Y"),
])

draw_fn = nx.draw_kamada_kawai

B_X_coeff = 2
B_D_coeff = 3
X_D_coeff = -7
X_A_coeff = 1.25
D_Y_coeff = 1
A_Y_coeff = -1
A_C_coeff = -1


def B_value():
    return 5 * uniform(-1, 1)

def X_value(b):
    return B_X_coeff * b + gauss(1, 2)

def D_value(b, x):
    return B_D_coeff * b + X_D_coeff * x + gauss(23, 0.25)

def A_value(x):
    return X_A_coeff * x + gauss(1, 1)

def Y_value(d, a):
    return D_Y_coeff * d + A_Y_coeff * a + gauss(9, 4)

def C_value(a):
    return A_C_coeff * a + gauss(2, 2)

def observation():
    b = B_value()
    x = X_value(b)
    d = D_value(b, x)
    a = A_value(x)
    y = Y_value(d, a)
    c = C_value(a)
    
    return (a, b, c, d, x, y)

