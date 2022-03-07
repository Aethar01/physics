import math
import statistics as s
import numpy as np
from scipy import stats, optimize as opt, special
from matplotlib import pyplot as plt

def getData(filename):
    a, b, c = np.genfromtxt(filename, \
                                        unpack = True, \
                                        usecols = (0, 1, 2), \
                                        comments = '#', \
                                        dtype = str)

    f = [eval(x) for x in a]
    Vin = [eval(x) for x in b]
    Vout = [eval(x) for x in c]
    return f, Vin, Vout

data1 = getData("data1")

for x in range(len(data1[2])):
    data1[2][x] = data1[2][x] / 1000

voutvin = []
for x in range(len(data1[1])):
    voutvin.append(data1[2][x] / data1[1][x])
    
sem1list = []
sem1 = stats.sem(voutvin)
for x in range(len(voutvin)):
    sem1list.append(sem1)

def plot(x, y, sem, optimized):
    plt.xlabel("Frequency (kHz)")
    plt.ylabel("$V_{out}\  /\  V_{in}$")
    plt.errorbar(x, y, xerr=None, yerr=sem, ls='None')
    plt.plot(x, y, marker='.')
    # plt.plot(x, func1(x, optimized[0], optimized[1]), '-', label="fit = $x^{}$ + {}".format(optimized[0].round(3), optimized[1].round(3)))
    # plt.legend()
    plt.show()

plot(data1[0], voutvin, sem1list, None)