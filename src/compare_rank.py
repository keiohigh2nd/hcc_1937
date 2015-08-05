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

def return_lines(filename):
  f = open(filename)
  lines = f.read().split('\r')
  f.close()

  return lines

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
  targets = 'COL8A2,TNFRSF11B,PRSS1,SDC2,NCAM1,CST3,COL6A3,OGN,EGFL6,CALML3,CXCL14,CLCA2,ELN,FGA,LYZL2,ALB,FGR,SH3GL3,CPA3,ITGAL,CPB2,KRT31,OMD,GYPA,TINAG,OSM,KRT1,BGN,UTS2,KLK7,KLK5'
  
  t_lists = targets.split(',')
  for t in t_lists:
    if int(query.find(t)) != -1:
      return 1
  return 0

def add_edgelist(G, lists):
  i = 0
  for l in lists:
    i += 1
    if i > 800:
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

  hcc_genes = 'data/HCC_origin_top50.csv'
  luc_genes = 'data/Luc_origin_top50.csv'
  hcc_mix_genes = 'data/exact_hcc_mix1_mix2.csv'
  luc_mix_genes = 'data/exact_luc_mix1_mix2.csv'
  
  hcc_nodes = return_nodelist(hcc_genes)
  luc_nodes = return_nodelist(luc_genes)
  luc_mix_nodes = return_nodelist(luc_mix_genes)
  hcc_mix_nodes = return_nodelist(hcc_mix_genes)

  hcc_mix_lines = return_lines(hcc_mix_genes)
  luc_mix_lines = return_lines(luc_mix_genes)
  #print hcc_mix_nodes
 

  f_h = open('result/hcc_rank.txt', 'w')  
  for hcc_node in hcc_nodes:
    i = 0
    for hm in hcc_mix_lines:
      i += 1
      tmp = hm.split(',')
      if hcc_node == tmp[0]:
        f_h.write(hm)
        f_h.write('\r')
      else:
        continue
  f_h.close()

  f_l = open('result/luc_rank.txt', 'w')
  for luc_node in luc_nodes:
    i = 0
    for lm in luc_mix_lines:
      i += 1
      tmp = lm.split(',')
      if luc_node == tmp[0]:
        f_l.write(lm)
        f_l.write('\r')
      else:
        continue
  f_h.close()

