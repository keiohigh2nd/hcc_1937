from __future__ import division
import networkx as nx
import numpy as np
import math, random, datetime
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import calc, graph, draw, optimize, statistic_test, degree

if __name__ == '__main__':
    #parameter
    luc_node = 80
    hcc_node = 17
 
    time = 12

    luc_gro = 20
    hcc_gro = 3
    #immune_cell = 0.1

    #Generate Graph
    lucG = nx.barabasi_albert_graph(luc_node, luc_gro)
    hccG = nx.barabasi_albert_graph(hcc_node, hcc_gro)

    frequency = np.array([0.9, 0.1])
    G_combine =nx.Graph()
    G_combine = graph.merge_graph_by_rank(G_combine, hccG, lucG, frequency)

    #Time series cell volume
    LucN = []
    hccN = []

    #Number of initial cell 
    cell_order = 2
    LucN0 = 10**cell_order
    hccN0 = 10**cell_order
    LucN_init = 10**cell_order
    hccN_init = 10**cell_order


    for t in range(time):
      LucN.append(calc.convert_volume(LucN0))
      lucG = graph.update_graph(lucG, luc_gro)
      LucN0 = LucN_init*calc.calc_entropy(lucG, t+1)
      
    for t in range(time):
      hccN.append(calc.convert_volume(hccN0))
      hccG = graph.update_graph(hccG, hcc_gro)
      hccN0 = hccN_init*calc.calc_entropy(hccG, t+1)

    #Mix Number of cell
    MixN0 = 10**cell_order
    MixN_init = 10**cell_order
    mix_new = 5
    initial_populations = MixN0*frequency
    G_comb_gro = ((frequency*np.array([luc_gro, hcc_gro])).sum())/2
    MixN = []
    x = []
    for t in range(time):
      x.append(t)
      MixN.append(calc.convert_volume(MixN0))
      G_combine = graph.update_graph(G_combine, G_comb_gro)
      MixN0 = MixN_init*calc.calc_entropy(G_combine, t+1)


    #Cut-off HUB
    long_time = 15
    c_MixN0 = 10**cell_order
    c_MixN_init = 10**cell_order
    c_mix_new = 10
    c_initial_populations = c_MixN0*frequency
    c_G_comb_gro = ((frequency*np.array([luc_gro, hcc_gro])).sum())/2
    c_MixN = []
    c_x = []
    for t in range(long_time):
      c_x.append(t)
      c_MixN.append(calc.convert_volume(c_MixN0))
      c_G_combine = graph.update_graph_mix_new(G_combine, G_comb_gro, c_mix_new)
      if t > 5: #anti-drug
        decreased_G_combine = graph.cut_graph(c_G_combine)
        c_MixN0 = c_MixN_init*calc.calc_entropy(decreased_G_combine, t+1)
      if t > 12: #new drug
        decreased_G_combine = graph.cut_graph(c_G_combine)
        c_MixN0 = c_MixN_init*calc.calc_entropy(decreased_G_combine, t+1)
        print calc.calc_entropy(decreased_G_combine, t+1)
      else:
        c_MixN0 = c_MixN_init*calc.calc_entropy(c_G_combine, t+1)
     
    draw.effect(c_MixN) 

    #Simple Correlation
    #p0 = optimize.num_corrcoef(LucN, hccN, MixN)

    #Check_Degree
    #degree.find_degree_change(lucG, hccG, G_combine)

 
    #Number Correlation
    mm2 = 43
    #p1 = optimize.num_cell_corrcoef(LucN, hccN, MixN, mm2)

    #Number Correlation
    #p2 = optimize.num_volume_corrcoef(LucN, hccN, MixN, mm2)
    p2 = optimize.num_volume_corrcoef_cut(LucN, hccN, MixN, c_MixN, mm2)

    #CCC
    #statistic_test.ccc_test(LucN, hccN, MixN, mm2)

    """
    #Grow Ratio
    sim_ratio =  np.array(LucN)/np.array(MixN)
    raw_ratio = graph.read_data()
    p = optimize.corrcoef(raw_ratio, sim_ratio)

    draw.fig(x, hccN, LucN, MixN, MixN_1)
    """
