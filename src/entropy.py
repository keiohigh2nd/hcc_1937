from __future__ import division
import networkx as nx
import numpy as np
import math, random, datetime
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import calc, graph, draw

   
def regression(raw, sim):
    time_point = len(raw[0])
    sim_tmp = len(sim)/time_point

    diff = []
    for i in range(len(raw)):#each lane 
      for j in range(time_point):#timepoint cutinto number of raw
        if str(float(raw[i][j])) != str(float('inf')) and str(float(raw[i][j])) != str(float('nan')):
          #Consider More How to Compare ratios between ran and simulation
          #diff.append(raw[i][j]/sim[j*sim_tmp])
          diff.append(raw[i][j])

    return diff


def check_diff(raw, sim):
    time_point = len(raw[0])
    sim_tmp = len(sim)/time_point

    diff = []
    sim_p = []
    for i in range(len(raw)):#3 lane
      for j in range(time_point):# 1 lane
        if str(float(raw[i][j])) != str(float('inf')) and str(float(raw[i][j])) != str(float('nan')):
          #Consider More How to Compare ratios between ran and simulation
          diff.append((raw[i][j]-sim[j*sim_tmp])**2)
          sim_p.append(sim[j*sim_tmp])
        else:
          sim_p.append(sim[j*sim_tmp])

    """
    #Pvalue Check
    #Don't input nan in ratio list 
    raw[0] = check_nan(raw[0])
    print sim_p[0:8] 
    t,p = stats.ttest_rel(raw[0], sim_p[0:8])    
    print p
    """
    tmp = np.array(diff)
    return np.average(tmp)


def update_all_parameter(diff):
    #print 'each difference -  %s' % diff
    luc_node = int(30*diff)
    hcc_node = int(5)
    time = 100

    #parameter
    luc_gro = int(6*diff)
    hcc_gro = int(2)

    lucG = nx.barabasi_albert_graph(luc_node, luc_gro)
    hccG = nx.barabasi_albert_graph(hcc_node, hcc_gro)

    frequency = np.array([0.9, 0.1])
    G_combine =nx.Graph()
    G_combine = graph.merge_graph(G_combine, hccG, lucG, frequency)

    frequency_1 = np.array([0.5, 0.5])
    G_combine_1 =nx.Graph()
    G_combine_1 = graph.merge_graph(G_combine_1, hccG, lucG, frequency_1)


    #Time series cell volume
    LucN = []
    hccN = []

    #Number of initial cell 
    LucN0 = 100
    hccN0 = 100

    for t in range(time):
      LucN.append(calc.convert_volume(LucN0))
      lucG = graph.update_graph(lucG, luc_gro)
      LucN0 = LucN0*calc.calc_entropy(lucG)

    for t in range(time):
      hccN.append(calc.convert_volume(hccN0))
      hccG = graph.update_graph(hccG, hcc_gro)
      hccN0 = hccN0*calc.calc_entropy(hccG)

    #Mix Number of cell
    MixN0 = 100
    initial_populations = MixN0*frequency
    G_comb_gro = ((frequency*np.array([luc_gro, hcc_gro])).sum())/2
    MixN = []
    x = []
    for t in range(time):
      x.append(t)
      MixN.append(calc.convert_volume(MixN0))
      G_combine = graph.update_graph(G_combine, G_comb_gro)
      MixN0 = MixN0*calc.calc_entropy(G_combine)
 
    sim_ratio =  np.array(LucN)/np.array(MixN)
    return sim_ratio

if __name__ == '__main__':
    #parameter
    luc_node = 30
    hcc_node = 10 
    time = 100
    luc_gro = 6
    hcc_gro = 3

    #Generate Graph
    lucG = nx.barabasi_albert_graph(luc_node, luc_gro)
    hccG = nx.barabasi_albert_graph(hcc_node, hcc_gro)

    frequency = np.array([0.9, 0.1])
    G_combine =nx.Graph()
    G_combine = graph.merge_graph(G_combine, hccG, lucG, frequency)

    frequency_1 = np.array([0.5, 0.5])
    G_combine_1 =nx.Graph()
    G_combine_1 = graph.merge_graph(G_combine_1, hccG, lucG, frequency_1)

    #Time series cell volume
    LucN = []
    hccN = []

    #Number of initial cell 
    LucN0 = 100
    hccN0 = 100

    for t in range(time):
      LucN.append(calc.convert_volume(LucN0))
      lucG = graph.update_graph(lucG, luc_gro)
      LucN0 = LucN0*calc.calc_entropy(lucG)
      
    for t in range(time):
      hccN.append(calc.convert_volume(hccN0))
      hccG = graph.update_graph(hccG, hcc_gro)
      hccN0 = hccN0*calc.calc_entropy(hccG)

    #Mix Number of cell
    MixN0 = 100
    initial_populations = MixN0*frequency
    G_comb_gro = ((frequency*np.array([luc_gro, hcc_gro])).sum())/2
    MixN = []
    x = []
    for t in range(time):
      x.append(t)
      MixN.append(calc.convert_volume(MixN0))
      G_combine = graph.update_graph(G_combine, G_comb_gro)
      MixN0 = MixN0*calc.calc_entropy(G_combine)

    #Combine_1
    MixN0_1 = 100
    G_comb_gro_1 = ((frequency_1*np.array([luc_gro, hcc_gro])).sum())/2
    MixN_1 = []
    for t in range(time):
      MixN_1.append(calc.convert_volume(MixN0_1))
      G_combine_1 = graph.update_graph(G_combine_1, G_comb_gro_1)
      MixN0_1 = MixN0_1*calc.calc_entropy(G_combine_1)

    #Regression
    sim_ratio =  np.array(LucN)/np.array(MixN)
    raw_ratio = graph.read_data()
    diff = regression(raw_ratio, sim_ratio)

    #Finish condition
    for k in xrange(1):#iteration 
      for i in xrange(len(diff)):#timepoint difference 
        diff = regression(raw_ratio, sim_ratio)
        if str(float(diff[i])) != str(float('inf')) and str(float(diff[i])) != str(float('nan')):
          sim_ratio = update_all_parameter(diff[i])

      ave = check_diff(raw_ratio, sim_ratio)
      #Finish condition
      if ave <= float(0.01):
      #Finish condition
        print 'Finish'
      else:
        print ave


    draw.fig(x, hccN, LucN, MixN, MixN_1)
