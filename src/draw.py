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
    plt.savefig('result/ratio_fig_%s_%s_.png' % (str(d.day),  str(random.randint(1,1000))))
