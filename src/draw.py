import math, random, datetime
import matplotlib.pyplot as plt

def fig(x, hccN, LucN, MixN, MixN_1):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(x, hccN, 'b')
    ax.plot(x, LucN, 'g')
    ax.plot(x, MixN, 'r',linestyle="--")
    ax.plot(x, MixN_1, 'm',linestyle=":")

    d = datetime.datetime.today()
    plt.savefig('result/sim_%s_%s_.png' % (str(d.day),  str(random.randint(1,1000))))

def ratio_fig(raw, sim):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = []
    for t in range(len(sim)):
      x.append(t)
    
    ax.plot(x, raw[0], 'b')
    ax.plot(x, raw[1], 'g')
    #ax.plot(x, raw[2], 'r')
    ax.plot(x, sim, 'm',linestyle=":")

    d = datetime.datetime.today()
    plt.title("Ratio Comparison")
    plt.savefig('result/ratio_fig_%s_%s_.png' % (str(d.day),  str(random.randint(1,1000))))

def cells_fig(sim,  raw, text):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = []
    for t in range(len(sim)):
      x.append(t)

    ax.plot(x, raw[0], 'b', label = "%s-0" % text)
    ax.plot(x, raw[1], 'r', label = "%s-1" % text)
    ax.plot(x, raw[2], 'm', label = "%s-2" % text)
    ax.plot(x, sim, 'g', linestyle=":", label = "Simulation")
    plt.legend()
    d = datetime.datetime.today()
    plt.title("Number of Cell")
    plt.ylabel("cells")
    plt.xlabel("time")
    plt.savefig('result/cells_fig_%s_%s_%s_.png' % (text, str(d.day),  str(random.randint(1,1000))))

def all_cells_fig(LucN_p, r_LucN, MixN_p, r_MixN, hccN_p, r_hccN):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = []
    for t in range(len(LucN_p)):
      x.append(t)

    ax.plot(x, r_LucN[0], 'b', label = "Luc-0", linestyle=":" )
    ax.plot(x, r_LucN[1], 'b', label = "Luc-1", linestyle=":" )
    ax.plot(x, r_LucN[2], 'b', label = "Luc-2", linestyle=":" )
    ax.plot(x, LucN_p, 'b', label = "Sim-Luc")

    ax.plot(x, r_MixN[0], 'r', label = "Mix-0", linestyle=":")
    ax.plot(x, r_MixN[1], 'r', label = "Mix-1", linestyle=":")
    ax.plot(x, r_MixN[2], 'r', label = "Mix-2", linestyle=":")
    ax.plot(x, MixN_p, 'r', label = "Sim-Mix")

    ax.plot(x, r_hccN[0], 'm', label = "HCC-0", linestyle=":")
    ax.plot(x, r_hccN[1], 'm', label = "HCC-1", linestyle=":")
    ax.plot(x, r_hccN[2], 'm', label = "HCC-2", linestyle=":")
    ax.plot(x, hccN_p, 'm', label = "Sim-Hcc")

    plt.legend(loc="upper left")
    d = datetime.datetime.today()
    plt.title("Number of Cell")
    plt.ylabel("cells/volume")
    plt.xlabel("time")
    plt.savefig('result/all_cells_fig_%s_%s_.png' % (str(d.day),  str(random.randint(1,1000))))


def all_cells_fig_cut(LucN_p, r_LucN, MixN_p, r_MixN, hccN_p, r_hccN, c_MixN_p):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = []
    for t in range(len(LucN_p)):
      x.append(t)

    ax.plot(x, r_LucN[0], 'b', label = "Luc-0", linestyle=":" )
    ax.plot(x, r_LucN[1], 'b', label = "Luc-1", linestyle=":" )
    ax.plot(x, r_LucN[2], 'b', label = "Luc-2", linestyle=":" )
    ax.plot(x, LucN_p, 'b', label = "Sim-Luc")

    ax.plot(x, r_MixN[0], 'r', label = "Mix-0", linestyle=":")
    ax.plot(x, r_MixN[1], 'r', label = "Mix-1", linestyle=":")
    ax.plot(x, r_MixN[2], 'r', label = "Mix-2", linestyle=":")
    ax.plot(x, MixN_p, 'r', label = "Sim-Mix")

    ax.plot(x, c_MixN_p, 'g', label = "cut_off_Sim-Mix")

    ax.plot(x, r_hccN[0], 'm', label = "HCC-0", linestyle=":")
    ax.plot(x, r_hccN[1], 'm', label = "HCC-1", linestyle=":")
    ax.plot(x, r_hccN[2], 'm', label = "HCC-2", linestyle=":")
    ax.plot(x, hccN_p, 'm', label = "Sim-Hcc")

    plt.legend(loc="upper left")
    d = datetime.datetime.today()
    plt.title("Number of Cell")
    plt.ylabel("cells/volume")
    plt.xlabel("time")
    plt.savefig('result/cut_all_cells_fig_%s_%s_.png' % (str(d.day),  str(random.randint(1,1000))))

def effect(c_MixN):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = []
    for t in range(len(c_MixN)):
      x.append(t)

    ax.plot(x, c_MixN, 'b', label = "Effect-Sim-Luc")
    plt.legend(loc="upper left")
    d = datetime.datetime.today()
    plt.title("Number of Cell with cut-off effect")
    plt.ylabel("cells/volume")
    plt.xlabel("time")
    plt.savefig('result/scut_fig_%s_%s_.png' % (str(d.day),  str(random.randint(1,1000))))
