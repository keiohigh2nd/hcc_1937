import networkx as nx
import numpy as np
import math, random, datetime
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

def gompertz(d, t):
    b = 1000
    c = 1000
    tmp = math.exp(-c*t)
    print tmp
    return math.pow(b, tmp)

def entropy(dist):
    dist = np.asarray(dist)
    ent = np.nansum( dist *  np.log2( 1/dist ) )
    return ent

def centrality_distribution(G):
    centrality = nx.degree_centrality(G).values()
    centrality = np.asarray(centrality)
    centrality /= centrality.sum()
    return centrality

def calc_entropy(G, t):
  d = centrality_distribution(G)
  #return math.exp(entropy(d)/10*t - 0.05*t)
  return math.exp((entropy(d)/10)*t - (1/entropy(d))*t)
  #return gompertz((entropy(d)/10), t)

def convert_volume(m):
    vl = math.pow(m, 1.5)
    return vl

def find_max_nodes(G):
    list = nx.degree_centrality(G)
    res = sorted(list.items(), key=lambda x:x[1], reverse=True)
    #TOP 10% is only growth
    return res[0:int(G.number_of_nodes()*0.1)]

def add_edges(G, res, gro):
    num_nodes = nx.number_of_nodes(G)
    for i in range(int(gro)):
        tmp = random.randint(0,nx.number_of_nodes(G))
        for j in res:
          G.add_edge(tmp, j[0])
        G.add_node(num_nodes + i)
    return G

def add_random_edges(G, res, gro):
    num_nodes = nx.number_of_nodes(G)
    for i in range(int(gro)):
        tmp = random.randint(0,nx.number_of_nodes(G))
        for j in res:
          tmp_1 = random.randint(0,nx.number_of_nodes(G))
          G.add_edge(tmp, tmp_1)
        G.add_node(num_nodes + i)

    return G

def add_random_edges_nodes(G, res, gro, mix_new):
    num_nodes = nx.number_of_nodes(G)
    for i in range(int(gro)):
        tmp = random.randint(0,nx.number_of_nodes(G))
        for j in res:
          tmp_1 = random.randint(0,nx.number_of_nodes(G))
          G.add_edge(tmp, tmp_1)
        G.add_node(num_nodes + i)
 
    num_nodes = nx.number_of_nodes(G)
    mix_new_gro = 15
    for i in range(mix_new):
        G.add_node(num_nodes + i)
        for i in range(mix_new_gro):
          tmp = random.randint(0,num_nodes)
          G.add_edge(num_nodes + i, tmp)
      
    return G

