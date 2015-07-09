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
