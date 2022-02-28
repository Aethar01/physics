import math
import statistics as s
import numpy as np
from scipy import stats, optimize as opt, special
from matplotlib import pyplot as plt

def getData(filename):
    V, A = np.genfromtxt(filename, \
                                        unpack = True, \
                                        usecols = (0, 1), \
                                        comments = '#', \
                                        dtype = str)

    V = [eval(x) for x in V]
    A = [eval(x) for x in A]
    return V, A

data1 = getData('data1.txt')
data2 = getData('data2.txt')

poo = []
for x in range(len(data1[1])):
    poo.append(data1[1][x]*-1)

data1sem = []
sem1 = stats.sem(data1[1])

data2sem = []
sem2 = stats.sem(data2[1])

for x in range(len(data1[1])):
    data1sem.append(sem1)

for x in range(len(data2[1])):
    data2sem.append(sem2)

def func1(x, a, b):
    dog = []
    for i in range(len(x)):
        dog.append(x*a + b)
    return dog
poo1 = data2[0]
poo2 = data2[1]
# optimized1, pcov1 = opt.curve_fit(func1, data1[0], data1[1], sigma=data1sem, absolute_sigma=True)
optimized1 = None
# optimized2, pcov2 = opt.curve_fit(func1, poo1, poo2, sigma=data2sem, absolute_sigma=True)

def plot(x, y, sem, optimized):
    plt.xlabel("Volts (V)")
    plt.ylabel("Current (mA)")
    plt.errorbar(x, y, xerr=None, yerr=sem, ls='None')
    plt.plot(x, y, marker='.')
    # plt.plot(x, func1(x, optimized[0], optimized[1]), '-', label="fit = $x^{}$ + {}".format(optimized[0].round(3), optimized[1].round(3)))
    # plt.legend()
    plt.show()
def plot1(x, y, sem, optimized):
    plt.xlabel("Volts (V)")
    plt.ylabel("Current (mA)")
    plt.errorbar(x, y, xerr=None, yerr=sem, ls='None')
    plt.plot(x, y, marker='.')
    # plt.plot(x, func1(x, optimized[0], optimized[1]), '-', label="fit = $x^{}$ + {}".format(optimized[0].round(3), optimized[1].round(3)))
    # plt.legend()
    plt.show()
# plot(data1[0], poo, data1sem, optimized1)

def getData1(filename):
    V, A, ohm = np.genfromtxt(filename, \
                                        unpack = True, \
                                        usecols = (0, 1, 2), \
                                        comments = '#', \
                                        dtype = str)

    V = [eval(x) for x in V]
    A = [eval(x) for x in A]
    ohm = [eval(x) for x in ohm]
    return V, A, ohm

data3 = getData1('data3.txt')
data4 = getData1('data4.txt')
data5 = getData1('data5.txt')

power3 = []
for x in range(len(data3[1])):
    power3.append((data3[1][x]**2) * data3[0][x] / data3[1][x])

power4 = []
for x in range(len(data4[1])):
    power4.append((data4[1][x]**2) * data4[0][x] / data4[1][x])

power5 = []
for x in range(len(data5[1])):
    power5.append((data5[1][x]**2) * data5[0][x] / data5[1][x])

sem3val = stats.sem(power3)
sem4val = stats.sem(power4)
sem5val = stats.sem(power5)
sem3 = [sem3val]*len(power3)
sem4 = [sem4val]*len(power4)
sem5 = [sem5val]*len(power5)

def plot2(x, y, sem, optimized):
    plt.xlabel("Resistance ($\Omega$")
    plt.ylabel("Power (W)")
    plt.errorbar(x, y, xerr=None, yerr=sem, ls='None')
    plt.plot(x, y, marker='.')
    # plt.plot(x, func1(x, optimized[0], optimized[1]), '-', label="fit = $x^{}$ + {}".format(optimized[0].round(3), optimized[1].round(3)))
    # plt.legend()
    plt.show()

plot2(data3[2], power3, sem3, None)
plot2(data4[2], power4, sem4, None)
plot2(data5[2], power5, sem5, None)