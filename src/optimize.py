#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
import datetime, random
import scipy.optimize
import matplotlib.pyplot as plt
import graph, draw, calc
from matplotlib import cbook

def fit_exp(parameter, x, y):
    a = parameter[0]
    b = parameter[1]
    residual = y - (a * numpy.exp(b * x))
    return residual

def fit_exp_linear(parameter, x, y):
    a = parameter[0]
    b = parameter[1]
    residual = numpy.log(y) - (numpy.log(a) + b * x)
    return residual

def exp_string(a, b):
    return "$y = %0.4f e^{ %0.4f x}$" % (a, b)

def check_number_of_cells(sim, raw, text):
    for t in range(len(sim)):
      print 'Sim = %s -- Raw = %s ' % (sim[t], raw[0][t])
    draw.cells_fig(sim, raw, text)

def num_cell_corrcoef(LucN, hccN, MixN, mm2):
    #Raw Data
    r_LucN, r_hccN, r_MixN = graph.num_read_cells(mm2)

    #Adjustment of  Timeseries   
    time_point = len(r_LucN[0]) # Experiments
    sim_time_point = len(LucN) # Simulation time
    sim_tmp = (len(LucN)*0.66)/(time_point-1) #1.25

    #Simulation timepoint
    LucN_p = []
    hccN_p = []
    MixN_p = []

    for t in range(time_point):
      if t != 0:
        print int(sim_time_point*0.3 + round(t*sim_tmp))
        LucN_p.append(LucN[int(sim_time_point*0.3 + round(t*sim_tmp))])
        hccN_p.append(hccN[int(sim_time_point*0.3 + round(t*sim_tmp))])
        MixN_p.append(MixN[int(sim_time_point*0.3 + round(t*sim_tmp))])
      else:
        LucN_p.append(LucN[int(round(t*sim_tmp))])
        hccN_p.append(hccN[int(round(t*sim_tmp))])
        MixN_p.append(MixN[int(round(t*sim_tmp))])


    print 'Simulation vs Raw'
    print 'Luc' 
    print check_number_of_cells(LucN_p, r_LucN, 'Luc')
    print 'Mix'
    print check_number_of_cells(MixN_p, r_MixN, 'Mix')
    print 'hcc'
    print check_number_of_cells(hccN_p, r_hccN, 'HCC')
    draw.all_cells_fig(LucN_p, r_LucN, MixN_p, r_MixN, hccN_p, r_hccN)

    corr_Luc = []
    corr_hcc = []
    corr_Mix = []
    for i in range(len(r_LucN)): #times of experiments
      tmp_Luc = np.corrcoef(r_LucN[i], LucN_p)
      tmp_hcc = np.corrcoef(r_hccN[i], hccN_p)
      tmp_Mix = np.corrcoef(r_MixN[i], MixN_p)
      corr_Luc.append(tmp_Luc[0,1])
      corr_hcc.append(tmp_hcc[0,1])
      corr_Mix.append(tmp_Mix[0,1])

    print 'Average Correlation Luc = %s, HCC = %s, Mix ~ %s ' % (np.average(np.array(corr_Luc)), np.average(np.array(corr_hcc)), np.average(np.array(corr_Mix)))
    return 0


def num_volume_corrcoef(LucN, hccN, MixN, mm2):
    #Raw Data
    r_LucN, r_hccN, r_MixN = graph.num_read_volume()

    #Adjustment of  Timeseries   
    time_point = len(r_LucN[0]) # Experiments
    sim_time_point = len(LucN) # Simulation time
    sim_tmp = (len(LucN)*0.66)/(time_point-1) #1.25

    #Simulation timepoint
    LucN_p = []
    hccN_p = []
    MixN_p = []

    for t in range(time_point):
      if t != 0:
        print int(sim_time_point*0.3 + round(t*sim_tmp))
        LucN_p.append(LucN[int(sim_time_point*0.3 + round(t*sim_tmp))])
        hccN_p.append(hccN[int(sim_time_point*0.3 + round(t*sim_tmp))])
        MixN_p.append(MixN[int(sim_time_point*0.3 + round(t*sim_tmp))])
      else:
        LucN_p.append(LucN[int(round(t*sim_tmp))])
        hccN_p.append(hccN[int(round(t*sim_tmp))])
        MixN_p.append(MixN[int(round(t*sim_tmp))])


    print 'Simulation vs Raw'
    print 'Luc'
    LucN_v = check_number_of_volume(LucN_p, r_LucN, mm2,'Luc')
    print 'Mix'
    MixN_v = check_number_of_volume(MixN_p, r_MixN, mm2, 'Mix')
    print 'hcc'
    hccN_v = check_number_of_volume(hccN_p, r_hccN, mm2, 'HCC')
    draw.all_cells_fig(LucN_v, r_LucN, MixN_v, r_MixN, hccN_v, r_hccN)

def num_volume_corrcoef_cut(LucN, hccN, MixN, c_MixN, mm2):
    print c_MixN
    #Raw Data
    r_LucN, r_hccN, r_MixN = graph.num_read_volume()

    #Adjustment of  Timeseries   
    time_point = len(r_LucN[0]) # Experiments
    sim_time_point = len(LucN) # Simulation time
    sim_tmp = (len(LucN)*0.66)/(time_point-1) #1.25

    #Simulation timepoint
    LucN_p = []
    hccN_p = []
    MixN_p = []
    c_MixN_p = []

    for t in range(time_point):
      if t != 0:
        print int(sim_time_point*0.3 + round(t*sim_tmp))
        LucN_p.append(LucN[int(sim_time_point*0.3 + round(t*sim_tmp))])
        hccN_p.append(hccN[int(sim_time_point*0.3 + round(t*sim_tmp))])
        MixN_p.append(MixN[int(sim_time_point*0.3 + round(t*sim_tmp))])
        c_MixN_p.append(c_MixN[int(sim_time_point*0.3 + round(t*sim_tmp))])
      else:
        LucN_p.append(LucN[int(round(t*sim_tmp))])
        hccN_p.append(hccN[int(round(t*sim_tmp))])
        MixN_p.append(MixN[int(round(t*sim_tmp))])
        c_MixN_p.append(c_MixN[int(round(t*sim_tmp))])


    print 'Simulation vs Raw'
    print 'Luc'
    LucN_v = check_number_of_volume(LucN_p, r_LucN, mm2,'Luc')
    print 'Mix'
    MixN_v = check_number_of_volume(MixN_p, r_MixN, mm2, 'Mix')
    print 'hcc'
    hccN_v = check_number_of_volume(hccN_p, r_hccN, mm2, 'HCC')
    print 'cut-off-Mix'
    c_MixN_v = check_number_of_volume(c_MixN_p, r_MixN, mm2, 'c-Mix')

    #draw.all_cells_fig(LucN_v, r_LucN, MixN_v, r_MixN, hccN_v, r_hccN)
    draw.all_cells_fig_cut(LucN_v, r_LucN, MixN_v, r_MixN, hccN_v, r_hccN, c_MixN_v)



def num_corrcoef(LucN, hccN, MixN):
    #Raw Data
    r_LucN, r_hccN, r_MixN = graph.num_read_data()

    #Adjustment of  Timeseries   
    time_point = len(r_LucN[0]) # Experiments
    sim_time_point = len(LucN) # Simulation time
    sim_tmp = (len(LucN)*0.66)/(time_point-1) #1.25

    #Simulation timepoint
    LucN_p = []
    hccN_p = []
    MixN_p = []

    for t in range(time_point):
      if t != 0: 
        print int(sim_tim_point*0.3 + round(t*sim_tmp))
        LucN_p.append(LucN[int(sim_tim_point*0.3 + round(t*sim_tmp))])
        hccN_p.append(hccN[int(sim_tim_point*0.3 + round(t*sim_tmp))])
        MixN_p.append(MixN[int(sim_tim_point*0.3 + round(t*sim_tmp))])
      else:
        LucN_p.append(LucN[int(round(t*sim_tmp))])
        hccN_p.append(hccN[int(round(t*sim_tmp))])
        MixN_p.append(MixN[int(round(t*sim_tmp))])    

    corr_Luc = []
    corr_hcc = []
    corr_Mix = []
    for i in range(len(r_LucN)): #times of experiments
      tmp_Luc = np.corrcoef(r_LucN[i], LucN_p)
      tmp_hcc = np.corrcoef(r_hccN[i], hccN_p)
      tmp_Mix = np.corrcoef(r_MixN[i], MixN_p)
      corr_Luc.append(tmp_Luc[0,1])
      corr_hcc.append(tmp_hcc[0,1])
      corr_Mix.append(tmp_Mix[0,1])

    print corr_hcc
    print np.average(np.array(corr_Luc))
    print np.average(np.array(corr_hcc))
    print np.average(np.array(corr_Mix))
    return 0

def corrcoef(raw, sim):
    time_point = len(raw[0])#8
    sim_tmp = len(sim)/time_point #1.25
    sim_p = []
    for t in range(time_point):
        sim_p.append(sim[round(t*sim_tmp)])

    corr = []
    for i in range(len(raw)): #times of experiments
      if int(i) == int(2): # exclude outlier
         break
      tmp = np.corrcoef(raw[i], sim_p)
      corr.append(tmp[0,1])
    
    draw.ratio_fig(raw, sim_p)
    print corr
    return corr

def check_number_of_volume(sim, raw, mm2, text):
    sim_size = []
    for t in range(len(sim)):
      tmp = graph.calculate_mm3(sim[t], mm2)
      sim_size.append(tmp)
      print 'Sim size = %s/mm3 -- Raw size = %s/mm3 ' % (str(tmp), raw[0][t])
    return sim_size
    #draw.volume_fig(sim_size, raw, text)


def check_diff(raw, sim):
    time_point = len(raw[0])
    sim_tmp = float(len(sim)/time_point)


    diff = []
    sim_p = []
    for i in range(len(raw)):#3 lane
      for j in range(time_point):# 1 lane
        if str(float(raw[i][j])) != str(float('inf')) and str(float(raw[i][j])) != str(float('nan')):
          #Consider More How to Compare ratios between ran and simulation
          diff.append((raw[i][j]-sim[round(j*sim_tmp)])**2)
          sim_p.append(sim[round(j*sim_tmp)])
        else:
          sim_p.append(sim[round(j*sim_tmp)])
    tmp = np.array(diff)
    return np.average(tmp)

