from __future__ import division

import networkx as nx
import numpy as np
import math, random, datetime
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import calc

def update_graph(G, gro):
    target_nodes = calc.find_max_nodes(G)
    return calc.add_edges(G, target_nodes, gro)

def merge_graph(G, G1, G2, frequency):
    n1 = G1.number_of_edges()
    n2 = G2.number_of_edges()

    e1 = G1.edges()
    e2 = G2.edges()

    for i in range(int(n1*frequency[0])):
      tmp = random.randint(0,n1-1)
      G.add_edge(e1[tmp][0], e1[tmp][1])

    for i in range(int(n2*frequency[1])):
      tmp = random.randint(0,n2-1)
      G.add_edge(e2[tmp][0], e2[tmp][1])

    return G

def read_data():
    #3 samples per 7 time point
    luc_data = np.loadtxt('data/100-0.csv', delimiter=",")
    hcc_data = np.loadtxt('data/0-100.csv', delimiter=",")
    mix_data = np.loadtxt('data/10-90.csv', delimiter=",", skiprows = 1)
    return luc_data/mix_data
