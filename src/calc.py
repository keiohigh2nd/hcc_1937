import networkx as nx
import numpy as np
import math, random, datetime
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

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
  print entropy(d)
  #return math.exp(entropy(d)/10*t - 0.05*t)
  return math.exp(entropy(d)/10*t - (1/entropy(d))*t)

def convert_volume(m):
    vl = math.pow(m, 1.5)
    return vl

def find_max_nodes(G):
    list = nx.degree_centrality(G)
    res = sorted(list.items(), key=lambda x:x[1], reverse=True)
    #TOP 10% is only growth
    return res[0:int(G.number_of_nodes()*0.1)]

def add_edges(G, res, gro):
    for i in range(int(gro)):
        tmp = random.randint(0,nx.number_of_nodes(G))
        for j in res:
          G.add_edge(tmp, j[0])

    return G

def add_random_edges(G, res, gro):
    for i in range(int(gro)):
        tmp = random.randint(0,nx.number_of_nodes(G))
        for j in res:
          tmp_1 = random.randint(0,nx.number_of_nodes(G))
          G.add_edge(tmp, tmp_1)

    return G

