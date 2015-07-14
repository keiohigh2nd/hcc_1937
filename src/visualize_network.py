import networkx as nx
import matplotlib.pyplot as plt
import csv
import itertools


h_targets = ['CXCR4','CYBB','VCAM1','TNFSF4']
m_targets = ['TLR2','CCL17','CCR7','ITPR2','TPH2','POLE']
im_edges = list(itertools.combinations(h_targets + m_targets ,2))

G=nx.Graph()

f = open('data/human_mouse_edge.csv')
lines = f.read().split('\r')
f.close()

for line in lines:
  tmp = line.split(',')
  G.add_edge(tmp[0], tmp[1],weight=float(tmp[2].strip('\r')))

plt.figure(1,figsize=(40,40))

#Form of Graph
#pos=nx.spring_layout(G) 
pos=nx.graphviz_layout(G,prog="dot")
#pos=nx.graphviz_layout(G)
#pos=nx.graphviz_layout(G,prog='twopi',args='')


nx.draw_networkx_nodes(G,pos,
                       nodelist=h_targets,
                       node_color='r',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(G,pos,
                       nodelist=m_targets,
                       node_color='b',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_edges(G,pos,
                       edgelist=im_edges,
                       width=8,alpha=0.5,edge_color='g')

nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.8)

#label
nx.draw_networkx_labels(G,pos,font_size=14, fontweight='bold')

#ouput
plt.axis('off')
plt.savefig("result/human_mouse_interaction.png") 

