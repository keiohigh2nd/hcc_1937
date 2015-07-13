from __future__ import division
import networkx as nx
import numpy as np
import math, random, datetime
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import calc, graph, draw, optimize

def ccc_test(LucN, hccN, MixN, mm2):
    r_LucN, r_hccN, r_MixN = graph.num_read_cells(mm2)

    time_point = len(r_LucN[0])#8
    num_experiments = len(r_LucN)
    sim_tmp = len(LucN)/time_point #1.25

    LucN_p = []
    hccN_p = []
    MixN_p = []
    for t in range(time_point):
        LucN_p.append(LucN[int(round(t*sim_tmp))])
        hccN_p.append(hccN[int(round(t*sim_tmp))])
        MixN_p.append(MixN[int(round(t*sim_tmp))])

    
    ave_LucN_r = np.average(r_LucN, axis=0)
    var_LucN_r = np.var(r_LucN, axis=0) 

    ccc = []
    for t in range(len(r_LucN[0])):#timepoint
      numerator = 0
      for j in range(num_experiments):#experiment
        numerator += (r_LucN[j][t]-ave_LucN_r[t])*1

      denominator = var_LucN_r[t]**2 + 1 + (ave_LucN_r[t] - LucN_p[t])**2
      tmp = 2*numerator/(denominator*num_experiments)
      ccc.append(tmp)
    print ccc

def exp_test():
    #parameter
    luc_node = 100
    time = 10
    luc_gro = 10

    #Generate Graph
    lucG = nx.barabasi_albert_graph(luc_node, luc_gro)

    #Time series cell volume
    LucN = []

    #Number of initial cell 
    LucN0 = 100
    LucN_init = 100

    mm2 = 43

    for t in range(time):
      LucN.append(calc.convert_volume(LucN0))
      lucG = graph.update_graph(lucG, luc_gro)
      LucN0 = LucN_init*math.exp(1/10*(t+1))

    r_LucN, r_hccN, r_MixN = graph.num_read_cells(mm2)

    time_point = len(r_LucN[0])#8
    sim_tmp = len(LucN)/time_point #1.25

    LucN_p = []
    for t in range(time_point):
        LucN_p.append(LucN[int(round(t*sim_tmp))])

    corr_Luc = []
    for i in range(len(r_LucN)): #times of experiments
      tmp_Luc = np.corrcoef(r_LucN[i], LucN_p)
      corr_Luc.append(tmp_Luc[0,1])

    print np.average(np.array(corr_Luc))
    return 0

if __name__ == '__main__':
  exp_test()
