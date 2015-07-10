#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
import datetime, random
import scipy.optimize
import matplotlib.pyplot as plt
import graph, draw
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

def num_corrcoef(LucN, hccN, MixN):
    r_LucN, r_hccN, r_MixN = graph.num_read_data()

    time_point = len(r_LucN[0])#8
    sim_tmp = len(LucN)/time_point #1.25

    LucN_p = []
    hccN_p = []
    MixN_p = []
    for t in range(time_point):
        LucN_p.append(LucN[int(round(t*sim_tmp))])
        hccN_p.append(hccN[int(round(t*sim_tmp))])
        MixN_p.append(MixN[int(round(t*sim_tmp))])


    corr = []
    for i in range(len(r_LucN)): #times of experiments
      tmp_Luc = np.corrcoef(r_LucN[i], LucN_p)
      tmp_hcc = np.corrcoef(r_hccN[i], hccN_p)
      tmp_Mix = np.corrcoef(r_MixN[i], MixN_p)
      corr.append(tmp_Luc[0,1])
      corr.append(tmp_hcc[0,1])
      corr.append(tmp_Mix[0,1])

    print corr
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

if __name__ == "__main__":
    x,y = graph.opt_read_data(2)

    print x
    print y
    parameter0 = [1, 0.03]
    r1 = scipy.optimize.leastsq(fit_exp, parameter0, args=(x, y))
    r2 = scipy.optimize.leastsq(fit_exp_linear, parameter0, args=(x, y))

    model_func = lambda a, b, x: a * numpy.exp(b * x)

    fig = plt.figure()

    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(x, y, "ro")
    ax2.plot(x, y, "ro")

    xx = numpy.arange(0.7, 0.2, -0.01)

    print r1
    ax1.plot(xx, model_func(r1[0][0], r1[0][1], xx))
    ax2.plot(xx, model_func(r2[0][0], r2[0][1], xx))

    #ax1.legend(("Sample Data", "Fitted Function:\n" + exp_string(r1[0][0], r1[0][1])),"upper left")
    #ax2.legend(("Sample Data", "Fitted Function:\n" + exp_string(r2[0][0], r2[0][1])), "upper left")

    ax1.set_title("Non-linear fit")
    ax2.set_title("Linear fit")

    ax1.grid(True)
    ax2.grid(True)

    #plt.show()
    d = datetime.datetime.today()
    plt.savefig('result/opt_%s_%s_.png' % (str(d.day),  str(random.randint(1,1000))))
