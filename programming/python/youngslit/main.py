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

    x = [eval(x) for x in a]
    mag1 = [eval(x) for x in b]
    mag2 = [eval(x) for x in c]
    return x, mag1, mag2

x, mag1, mag2 = getData('data1.txt')[0], getData('data1.txt')[1], getData('data1.txt')[2]
mag = []
for i in range(len(mag1)):
    mag.append((mag1[i] + mag2[i]) / 2)

magcom = list(zip(mag1, mag2))

def plot(x, y, sem, optimized, xname=None, yname=None):
    plt.figure(dpi=1200)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.errorbar(x, y, xerr=None, yerr=sem, ls='None')
    
    plt.plot(x, y, marker='x', ls='None')
    # plt.plot(x, func1(x, optimized[0], optimized[1]), '-', label="fit = $x^{}$ + {}".format(optimized[0].round(3), optimized[1].round(3)))
    # plt.legend()
    plt.show()

sem = []
for i in range(len(magcom)):
    sem.append(stats.sem(magcom[i]))

print(len(mag), len(x), len(magcom))

plot(x, mag, sem, None, 'Distance (cm)', 'Magnitude (mV)')

angle = []
for i in range(len(x)):
    angle.append(math.sin(math.atan((x[i]-49.6)/157)))

plot(angle, mag, sem, None, 'Sin$\\theta$', 'Magnitude (mV)')