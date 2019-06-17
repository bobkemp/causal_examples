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

X_B_coeff = 2
D_B_coeff = 3
D_X_coeff = -7
A_X_coeff = 1.25
Y_D_coeff = 1
Y_A_coeff = -1
C_A_coeff = -1


def B_value():
    return 5 * uniform(-1, 1)

def X_value(b):
    return X_B_coeff * b + gauss(1, 2)

def D_value(b, x):
    return D_B_coeff * b +D_X_coeff * x + gauss(23, 0.25)

def A_value(x):
    return A_X_coeff * x + gauss(1, 1)

def Y_value(d, a):
    return Y_D_coeff * d + Y_A_coeff * a + gauss(9, 4)

def C_value(a):
    return C_A_coeff * a + gauss(2, 2)

def observation():
    b = B_value()
    x = X_value(b)
    d = D_value(b, x)
    a = A_value(x)
    y = Y_value(d, a)
    c = C_value(a)
    
    return (a, b, c, d, x, y)

