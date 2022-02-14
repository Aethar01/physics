import math
import statistics as s
import numpy as np
from scipy import stats, optimize as opt, special
from matplotlib import pyplot as plt


def getData(filename):
    temp_1, W_1, temp_2, W_2 = np.genfromtxt(filename, \
                                        unpack = True, \
                                        usecols = (0, 1, 2, 3), \
                                        comments = '#', \
                                        dtype = str)

    temp_1 = [eval(x) for x in temp_1]
    W_1 = [eval(x) for x in W_1]
    temp_2 = [eval(x) for x in temp_2]
    W_2 = [eval(x) for x in W_2]
    return temp_1, W_1, temp_2, W_2

data = getData("data.txt")


data[1].remove(0)
data[0].remove(0)
sem_1 = stats.sem(data[1])

def func21(x, a, b):
    dog = []
    for i in range(len(x)):
        dog.append((x[i] * a) + b)
    return dog

sem_1list = []

for x in range(len(data[1])):
    sem_1list.append(sem_1)

optimized, pcov = opt.curve_fit(func, data[0], data[1], sigma=sem_1list, absolute_sigma=True)

plt.title("W against $T_h - T_c$ for 10V and 12$\pm$0.1A over 5 minutes")
plt.xlabel("$T_h - T_c$ ($\degree C$)")
plt.ylabel("Work per revolution (hPa$cm^3$)")
plt.errorbar(data[0], data[1], xerr=None, yerr=sem_1, ls='None')
plt.scatter(data[0], data[1], marker='.', label="10V and 12$\pm$0.1A")
plt.plot(data[0], func21(data[0], optimized[0], optimized[1]), '-', label="fit = {}x + {}".format(optimized[0].round(3), optimized[1].round(3)))
plt.legend()


sem_2 = stats.sem(data[3])

sem_2list = []

for x in range(len(data[2])):
    sem_2list.append(sem_2)

optimized, pcov = opt.curve_fit(func, data[2], data[3], sigma=sem_2list, absolute_sigma=True)

plt.title("W against $T_h - T_c$ for 6V and 9$\pm$0.1A over 5 minutes")
plt.xlabel("$T_h - T_c$ ($\degree C$)")
plt.ylabel("Work per revolution (hPa$cm^3$)")
plt.errorbar(data[2], data[3], xerr=None, yerr=sem_2, ls='None')
plt.scatter(data[2], data[3], marker='.', label="6V and 9$\pm$0.1A")
plt.plot(data[2], func21(data[2], optimized[0], optimized[1]), '-', label="fit = {}x + {}".format(optimized[0].round(3), optimized[1].round(3)))
plt.legend()


plt.title("Both plots")