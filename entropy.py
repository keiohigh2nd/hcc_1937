from __future__ import division

import networkx as nx
import numpy as np
import math, random
import matplotlib.pyplot as plt

G1_node = 20
G2_node = 200
G1_gro = 2
G2_gro = 10

def entropy(dist):
    dist = np.asarray(dist)
    ent = np.nansum( dist *  np.log2( 1/dist ) )
    return ent

def centrality_distribution(G):
    centrality = nx.degree_centrality(G).values()
    centrality = np.asarray(centrality)
    centrality /= centrality.sum()
    return centrality
                                         
def calc_entropy(G):
  d = centrality_distribution(G)
  return math.exp(entropy(d)/10)

def convert_volume(m):
    vl = math.pow(m, 1.5)
    return vl

def find_max_nodes(G):
    list = nx.degree_centrality(G)
    res = sorted(list.items(), key=lambda x:x[1], reverse=True)
    return res[0:int(G.number_of_nodes()*0.1)]

def add_edges(G, res, gro):
    for i in range(int(gro)):
        tmp = random.randint(0,nx.number_of_nodes(G))
        for j in res:
          G.add_edge(tmp, j[0])

    return G

def update_graph(G, gro):
    target_nodes = find_max_nodes(G)
    return add_edges(G, target_nodes, gro)

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

if __name__ == '__main__':
    luc_node = 100
    hcc_node = 3
    luc_gro = 50
    hcc_gro = 2

    lucG = nx.barabasi_albert_graph(luc_node, luc_gro)
    hccG = nx.barabasi_albert_graph(hcc_node, hcc_gro)

    frequency = np.array([0.9, 0.1])
    G_combine =nx.Graph()
    G_combine = merge_graph(G_combine, hccG, lucG, frequency)

    time = 10
    #Time series cell volume
    LucN = []
    hccN = []

    #Number of initial cell 
    LucN0 = 100
    hccN0 = 100

    for t in range(time):
      LucN.append(convert_volume(LucN0))
      lucG = update_graph(lucG, luc_gro)
      LucN0 = LucN0*calc_entropy(lucG)
      
    for t in range(time):
      hccN.append(convert_volume(hccN0))
      hccG = update_graph(hccG, hcc_gro)
      hccN0 = hccN0*calc_entropy(hccG)

    #Mix Number of cell
    MixN0 = 100
    initial_populations = MixN0*frequency
    G_comb_gro = ((frequency*np.array([luc_gro, hcc_gro])).sum())/2
    print G_comb_gro
    MixN = []
    x = []
    for t in range(time):
      x.append(t)
      MixN.append(convert_volume(MixN0))
      G_combine = update_graph(G_combine, G_comb_gro)
      MixN0 = MixN0*calc_entropy(G_combine)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(x, hccN, 'b')
    ax.plot(x, LucN, 'g')
    ax.plot(x, MixN, 'r',linestyle="--")

    plt.savefig('test.png')
    plt.close()
