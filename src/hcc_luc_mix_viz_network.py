import networkx as nx
import matplotlib.pyplot as plt
import csv, datetime, random
import itertools

def return_edgelist(filename):
  f = open(filename)
  lines = f.read().split('\r')
  f.close()

  edges = []
  for line in lines:
    tmp = line.split(',')
    #G.add_edge(tmp[0], tmp[1],weight=float(tmp[2].strip('\r')))
    edges.append((tmp[0], tmp[1]))
  return edges

def add_edgelist(G, lists):
  for l in lists:
    G.add_node(l[0])
    G.add_node(l[1])
  return G
if __name__ == '__main__':

  hcc_network = 'data/hcc_origin_top50_genemania.csv'
  luc_network = 'data/luc_origin_top50_genemania.csv'
  mix_network = 'data/genemania_network_hcc_luc_vs_mix_sum.csv'
  
  hcc_edges = return_edgelist(hcc_network)
  luc_edges = return_edgelist(luc_network)
  mix_edges = return_edgelist(mix_network)

  G=nx.Graph()
  G = add_edgelist(G, hcc_edges)
  G = add_edgelist(G, luc_edges)
  G = add_edgelist(G, mix_edges)


  plt.figure(1,figsize=(40,40))

  #Form of Graph
  #pos=nx.spring_layout(G) 
  #pos=nx.graphviz_layout(G,prog="dot")
  #pos=nx.graphviz_layout(G)
  pos=nx.graphviz_layout(G,prog='twopi',args='')


  nx.draw_networkx_nodes(G,pos,
                         nodelist=G.nodes(),
                         node_color='b',
                         node_size=300,
                         alpha=0.8)


  nx.draw_networkx_edges(G,pos,
                         edgelist=hcc_edges,
                         width=8,alpha=0.5,edge_color='g')

  nx.draw_networkx_edges(G,pos,
                         edgelist=luc_edges,
                         width=6,alpha=0.5,edge_color='r')

  nx.draw_networkx_edges(G,pos,
                         edgelist=mix_edges,
                         width=4,alpha=0.5,edge_color='b')


  #nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.8)

  #label
  nx.draw_networkx_labels(G,pos,font_size=14, fontweight='bold')

  #ouput
  plt.axis('off')
  d = datetime.datetime.today()
  plt.savefig("result/hcc_luc_mix_interaction_%s_%s.png"% (str(d.day),  str(random.randint(1,1000))))
 
