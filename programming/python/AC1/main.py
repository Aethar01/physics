import math
import statistics as s
import numpy as np
from scipy import stats, optimize as opt, special
from matplotlib import pyplot as plt


def getData(filename):
    freq, V_in, V_out, phase = np.genfromtxt(filename, \
                                        unpack = True, \
                                        usecols = (0, 1, 2, 3), \
                                        comments = '#', \
                                        dtype = str)

    freq = [eval(x) for x in freq]
    V_in = [eval(x) for x in V_in]
    V_out = [eval(x) for x in V_out]
    phase = [eval(x) for x in phase]
    return freq, V_in, V_out, phase

data1 = getData('data1.txt')
data2 = getData('data2.txt')

def magnitude(data):
    logdataset = []
    for x in range(len(data[1])):
        logdataset.append(20 * np.log10(data[1][x] / data[2][x]))
    return logdataset

magdata1 = magnitude(data1)
magdata2 = magnitude(data2)

semmag1 = []
sem1 = stats.sem(magdata1)

semmag2 = []
sem2 = stats.sem(magdata2)

for x in range(len(magdata1)):
    semmag1.append(sem1)

for x in range(len(magdata2)):
    semmag2.append(sem2)

def func1(x, a, b):
    dog = []
    for i in range(len(x)):
        dog.append(-20 * np.log10(x[i] * a) + b)
    return dog

optimized1, pcov1 = opt.curve_fit(func1, data1[0], magdata1, sigma=semmag1, absolute_sigma=True)


def magplot(x, y, sem, optimized):
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.errorbar(x, y, xerr=None, yerr=sem, ls='None')
    plt.plot(x, y, marker='.')
    # plt.plot(x, func1(x, optimized[0], optimized[1]), '-', label="fit = {}x + {}".format(optimized[0].round(3), optimized[1].round(3)))
    # plt.legend()
    plt.show()

magplot(data1[0], magdata1, semmag1, optimized1)

optimized2, pcov2 = opt.curve_fit(func1, data2[0], magdata2, sigma=semmag2, absolute_sigma=True)

magplot(data2[0], magdata2, semmag2, optimized2)

def phaseplot(x, y, sem):
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase ($\degree$)")
    plt.errorbar(x, y, xerr=None, yerr=sem, ls='None')
    plt.plot(x, y, marker='.')
    # plt.plot(x, func1(x, optimized[0], optimized[1]), '-', label="fit = {}x + {}".format(optimized[0].round(3), optimized[1].round(3)))
    # plt.legend()
    plt.show()

semphase1 = []
semphase2 = []

for x in range(len(data1[3])):
    semphase1.append(stats.sem(data1[3]))
for x in range(len(data2[3])):
    semphase2.append(stats.sem(data2[3]))

phaseplot(data1[0], data1[3], semphase1)
phaseplot(data2[0], data2[3], semphase2)