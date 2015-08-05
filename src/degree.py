from __future__ import division

import networkx as nx
import numpy as np
import math, random, datetime
import scipy as sp
from scipy import stats
import calc
import matplotlib.pyplot as plt

def degree_histogram(G, text):
  degree_sequence=sorted(nx.degree(G).values(),reverse=True) # degree sequence
  #print "Degree sequence", degree_sequence
  dmax=max(degree_sequence)

  plt.loglog(degree_sequence,'b-',marker='o')
  plt.title("Degree rank")
  plt.ylabel("degree")
  plt.xlabel("rank")

  # draw graph in inset
  plt.axes([0.45,0.45,0.45,0.45])
  Gcc=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
  pos=nx.spring_layout(Gcc)
  plt.axis('off')
  nx.draw_networkx_nodes(Gcc,pos,node_size=20)
  nx.draw_networkx_edges(Gcc,pos,alpha=0.4)

  plt.savefig("result/degree_histogram_%s.png" % text)

def find_degree_change(luc, hcc, mix):
  hcc_list = nx.degree(hcc)
  luc_list = nx.degree(luc)
  mix_list = nx.degree(mix)
  
  hcc_num_nodes = nx.number_of_nodes(hcc)
  luc_num_nodes = nx.number_of_nodes(luc)
  mix_num_nodes = nx.number_of_nodes(mix)

  print luc_num_nodes

  for t in range(len(hcc_list)):
    print '%s ---- %s --- %s ---' % (hcc_list[t], luc_list[t], mix_list[t])
    if int(hcc_list[t]) <= hcc_num_nodes*0.15 and int(luc_list[t]) <= luc_num_nodes*0.15:
	if int(hcc_list[t]) >= mix_num_nodes*0.15:
          print "found"

  #Draw Degree Histogram  
  #degree_histogram(luc, 'luc')
  #degree_histogram(hcc, 'hcc')
  #degree_histogram(mix, 'mix')

if __name__ == '__main__':
  x,y = opt_read_data(2)
