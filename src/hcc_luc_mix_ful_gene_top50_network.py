import networkx as nx
import matplotlib.pyplot as plt
import csv, datetime, random
import itertools

def return_nodelist(filename):
  f = open(filename)
  lines = f.read().split('\r')
  f.close()

  nodes = []
  for line in lines:
    tmp = line.split(',')
    #G.add_edge(tmp[0], tmp[1],weight=float(tmp[2].strip('\r')))
    nodes.append(tmp[0])
  return nodes

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

def add_nodelist(G, lists):
  for l in lists:
    G.add_node(l)
  return G


def add_edgelist(G, lists):
  i = 0
  for l in lists:
    i += 1
    if i > 3000:
      break
    if int(l[0].find('orf')) != -1 or int(l[0].find('LOC'))!= -1:
      continue
    if int(l[1].find('orf')) != -1 or int(l[1].find('LOC'))!= -1:
      continue
    G.add_edge(l[0],l[1])
  return G

def read_cancer_gene(filename):
  f = open(filename)
  lines = f.read().split('\r')
  f.close()

  genes = []
  del lines[0]
  for line in lines:
    tmp = line.split(',')
    genes.append(tmp[1])
  return genes

if __name__ == '__main__':

  hcc_genes = 'data/HCC_origin_top50.csv'
  luc_genes = 'data/Luc_origin_top50.csv'
  mix_genes = 'data/hcc_luc_comp_mix_sum.csv'
  all_networks = 'data/hcc_luc_mix_genes_top50_genemania_network.csv'
  
  hcc_nodes = return_nodelist(hcc_genes)
  luc_nodes = return_nodelist(luc_genes)
  mix_nodes = return_nodelist(mix_genes)

  hcc_cancer_genes = read_cancer_gene('data/HCC_NCG_query_list.csv')
  luc_cancer_genes = read_cancer_gene('data/Luc_NCG_query_list.csv')
  mix_cancer_genes = read_cancer_gene('data/Mix_NCG_query_list.csv')

  all_edges = return_edgelist(all_networks)

  G=nx.Graph()
  G = add_edgelist(G, all_edges)
  G = add_nodelist(G, hcc_nodes)
  G = add_nodelist(G, luc_nodes)
  G = add_nodelist(G, mix_nodes)
  G = add_nodelist(G, hcc_cancer_genes)
  G = add_nodelist(G, luc_cancer_genes)
  G = add_nodelist(G, mix_cancer_genes)

  plt.figure(1,figsize=(80,80))

  #Form of Graph
  #pos=nx.spring_layout(G) 
  #pos=nx.graphviz_layout(G,prog="dot")
  #pos=nx.graphviz_layout(G)
  #pos=nx.graphviz_layout(G,prog='twopi',args='')
  pos=nx.graphviz_layout(G,prog="twopi",root=0)

  nx.draw_networkx_nodes(G,pos,
                         nodelist=hcc_nodes,
                         node_color='b',
                         node_size=50,
                         alpha=0.8)

  nx.draw_networkx_nodes(G,pos,
                         nodelist=hcc_cancer_genes,
                         node_color='b',
                         node_size=500,
                         alpha=0.8)


  nx.draw_networkx_nodes(G,pos,
                         nodelist=luc_nodes,
                         node_color='g',
                         node_size=50,
                         alpha=0.8)

  nx.draw_networkx_nodes(G,pos,
                         nodelist=luc_cancer_genes,
                         node_color='g',
                         node_size=500,
                         alpha=0.8)

  nx.draw_networkx_nodes(G,pos,
                         nodelist=mix_nodes,
                         node_color='r',
                         node_size=50,
                         alpha=0.8)

  nx.draw_networkx_nodes(G,pos,
                         nodelist=mix_cancer_genes,
                         node_color='r',
                         node_size=500,
                         alpha=0.8)



  nx.draw_networkx_edges(G,pos,
                         edgelist=G.edges(),
                         width=1, alpha=0.5, edge_color='k')




  #nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.8)

  #label
  nx.draw_networkx_labels(G,pos,font_size=14, fontweight='bold')

  #ouput
  plt.axis('off')
  d = datetime.datetime.today()
  plt.savefig("result/ful_top50_hcc_luc_mix_interaction_%s_%s.png"% (str(d.day),  str(random.randint(1,1000))))
 
