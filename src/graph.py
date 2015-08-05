from __future__ import division

import networkx as nx
import numpy as np
import math, random, datetime
import scipy as sp
from scipy import stats
import calc

def update_graph(G, gro):
    target_nodes = calc.find_max_nodes(G)
    #return calc.add_edges(G, target_nodes, gro)
    return calc.add_random_edges(G, target_nodes, gro)

def update_graph_mix_new(G, gro, mix_new):
    target_nodes = calc.find_max_nodes(G)
    return calc.add_random_edges_nodes(G, target_nodes, gro, mix_new)

def merge_graph(G, G1, G2, frequency):
    #HCC is 0.9, Luc is 0.1 make sure
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

def merge_graph_by_rank(G, G1, G2, frequency):
    #HCC is 0.9, Luc is 0.1 make sure
    n1 = G1.number_of_edges()
    n2 = G2.number_of_edges()

    e1 = G1.edges()
    e2 = G2.edges()

    for i in range(int(n1*frequency[0])):
      tmp = random.randint(0,n1-1)
      G.add_edge(e1[tmp][0], e1[tmp][1])

    target_nodes = calc.find_max_nodes(G2)
    print 'Top nodes'
    print target_nodes 

    for i in range(int(n2*frequency[1])):
      tmp = random.randint(0,n2-1)
      #Top target
      random_tmp = random.choice(target_nodes) 
      #Target of top targets
      random_tmp_target = random.choice(G2.neighbors(random_tmp[0]))
      G.add_edge(random_tmp[0], random_tmp_target)

    return G

def cut_graph(G):
    target_nodes = calc.find_max_nodes(G)
    for t in target_nodes:
      t_edges = G.neighbors(t[0])
      for t_e in t_edges:
        G.remove_edge(t[0], t_e)
      G.remove_node(t[0])
    return G


def num_read_data():
    luc_data = np.loadtxt('data/100-0_r.csv', delimiter=",")
    hcc_data = np.loadtxt('data/0-100_r.csv', delimiter=",")
    mix_data = np.loadtxt('data/10-90_r.csv', delimiter=",", skiprows = 1)
    return luc_data, hcc_data, mix_data

def num_read_cells(mm2):
    mm3 = calc.convert_volume(mm2)*10**3
    luc_data = np.loadtxt('data/100-0_r.csv', delimiter=",") + 1
    hcc_data = np.loadtxt('data/0-100_r.csv', delimiter=",") + 1
    mix_data = np.loadtxt('data/10-90_r.csv', delimiter=",", skiprows = 1) + 1
   
    return luc_data*mm3, hcc_data*mm3, mix_data*mm3
def num_read_volume():
    luc_data = np.loadtxt('data/100-0_r.csv', delimiter=",") + 1
    hcc_data = np.loadtxt('data/0-100_r.csv', delimiter=",") + 1
    mix_data = np.loadtxt('data/10-90_r.csv', delimiter=",", skiprows = 1) + 1

    return luc_data, hcc_data, mix_data

def calculate_mm3(cells, mm2):
    cells_per_mm3 = calc.convert_volume(mm2)*10*3
    return cells/cells_per_mm3

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

if __name__ == '__main__':
  x,y = opt_read_data(2)
