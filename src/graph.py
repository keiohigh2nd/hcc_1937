from __future__ import division

import networkx as nx
import numpy as np
import math, random, datetime
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

def num_read_data():
    luc_data = np.loadtxt('data/100-0_r.csv', delimiter=",")
    hcc_data = np.loadtxt('data/0-100_r.csv', delimiter=",")
    mix_data = np.loadtxt('data/10-90_r.csv', delimiter=",", skiprows = 1)
    return luc_data, hcc_data, mix_data

def read_data():
    #3 samples per 7 time point
    luc_data = np.loadtxt('data/100-0_r.csv', delimiter=",")
    hcc_data = np.loadtxt('data/0-100_r.csv', delimiter=",")
    mix_data = np.loadtxt('data/10-90_r.csv', delimiter=",", skiprows = 1)
    return luc_data/mix_data

def opt_read_data(i):
    luc_data = np.loadtxt('data/100-0.csv', delimiter=",")
    hcc_data = np.loadtxt('data/0-100.csv', delimiter=",")
    mix_data = np.loadtxt('data/10-90.csv', delimiter=",", skiprows = 1)
    tp = len(mix_data[0])
    x = []
    for i in range(3):
      for t in range(tp):
        x.append(t)
    
    luc_data = luc_data.reshape(24)
    mix_data = mix_data.reshape(24)
    return np.array(x), luc_data
    """
    for i in range(len(luc_data)):
      if luc_data[i] == 0:
        luc_data[i] =  0.000000001
      if mix_data[i] == 0:
        mix_data[i] = 0.0000000001

    print 'finish'
    if int(i) == int(1):
      return np.array(x), luc_data
    if int(i) == int(2):
      return np.array(x), mix_data
    """

if __name__ == '__main__':
  x,y = opt_read_data(2)
