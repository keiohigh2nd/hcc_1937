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

def special_list(query):

  #matrix
  #targets = 'COL8A2,TNFRSF11B,PRSS1,SDC2,NCAM1,CST3,COL6A3,OGN,EGFL6,CALML3,CXCL14,CLCA2,ELN,FGA,LYZL2,ALB,FGR,SH3GL3,CPA3,ITGAL,CPB2,KRT31,OMD,GYPA,TINAG,OSM,KRT1,BGN,UTS2,KLK7,KLK5'
  
  #calcium
  #targets = 'CHP2,EGFL6,CDH22,CALML3,RCVRN,MYL3,BGN'

  #extra region
  targets = 'CD79B,OGN,GDF6,EGFL6,FRZB,SFTPA2,PRKAG3,CALML3,AOAH,FREM3,CHRDL2,CXCL14,KLK3,PSG11,CLCA2,ELN,ANXA13,AFM,CCDC70,PRG4,NCAN,FGA,OR11L1,LYZL2,THY1,DPYS,IL17C,FASLG,IL22RA2,CHGB,ADH7,CRH,ALB,FGR,SH3GL3,C12ORF39,SCGN,ACSM1,PON1,FAT2,CPA3,ITGAL,DKK4,CPB2,KRT31,SFTPA1,OMD,TAC3,GYPA,MEP1A,CXCL11,TINAG,SPINK8,OSM,KRT1,PRB3,CNTF,KCNG2,BGN,UTS2'

  t_lists = targets.split(',')
  for t in t_lists:
    if int(query.find(t)) != -1:
      return 1
  return 0

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
    #Specific Condition
    if special_list(l[0]) == 1:
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

  hcc_genes = 'data/KRT_HCC.csv'
  luc_genes = 'data/KRT_LUC.csv'
  mix_genes = 'data/KRT_mix.csv'
  all_networks = 'data/KRT_genenetwork.csv'
  
  hcc_nodes = return_nodelist(hcc_genes)
  luc_nodes = return_nodelist(luc_genes)
  mix_nodes = return_nodelist(mix_genes)

  all_edges = return_edgelist(all_networks)

  G=nx.Graph()
  G = add_edgelist(G, all_edges)
  G = add_nodelist(G, hcc_nodes)
  G = add_nodelist(G, luc_nodes)
  G = add_nodelist(G, mix_nodes)

  plt.figure(1,figsize=(50,50))

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
                         nodelist=luc_nodes,
                         node_color='g',
                         node_size=50,
                         alpha=0.8)


  nx.draw_networkx_nodes(G,pos,
                         nodelist=mix_nodes,
                         node_color='r',
                         node_size=50,
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
  plt.savefig("result/krt_gene_interaction_%s_%s.png"% (str(d.day),  str(random.randint(1,1000))))
 
