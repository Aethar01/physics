import math
import statistics as s
import numpy as np
from scipy import stats, optimize as opt, special
from matplotlib import pyplot as plt


def getData(filename):
    ten, thirty, fifty, seventy, ninety = np.genfromtxt(filename, \
                                        unpack = True, \
                                        usecols = (0, 1, 2, 3, 4), \
                                        comments = '#', \
                                        dtype = str)

    ten = [eval(x) for x in ten]
    thirty = [eval(x) for x in thirty]
    fifty = [eval(x) for x in fifty]
    seventy = [eval(x) for x in seventy]
    ninety = [eval(x) for x in ninety]
    return ten, thirty, fifty, seventy, ninety

data = getData("ex2.txt")

databy10 = []
for x in range(len(data)):
    databy101 = []
    for i in range(len(data[x])):
        databy101.append(data[x][i] / 10)
    databy10.append(databy101)

datamean = []

for x in range(len(data)):
    datamean.append(np.mean(databy10[x]))

datameansq = []

for x in range(len(datamean)):
    datameansq.append(datamean[x] ** 2)

plengths = [0.1, 0.3, 0.5, 0.7, 0.9]

databy10sem = []

for x in range(len(data)):
    databy10sem.append(2 * stats.sem(databy10[x]))

# print(databy10sem)
# print(datameansq)
def func(x, a):
    return a * x

optimized, pcov = opt.curve_fit(func, plengths, datameansq, sigma=databy10sem, absolute_sigma=True)

plt.title("$T^2$ against L")
plt.xlabel("Pendulum length (M)")
plt.ylabel("Time period$^2$ (s)")
plt.errorbar(plengths, datameansq, xerr=None, yerr=databy10sem, ls='None')
plt.scatter(plengths, datameansq, marker='.', label="data")
plt.plot(plengths, func(plengths, optimized), '-', label="fit")
plt.legend()


plt.show()

print("y = {}x".format(optimized))
for x in range(len(data)):
    print("for length {}, T^2 is {} +- {}".format(plengths[x], datameansq[x].round(3), databy10sem[x].round(3)))


gvalues = []

for x in range(len(data)):
    gvalues.append((plengths[x] * (((2 * np.pi) / datamean[x]) ** 2)))
print(gvalues)



pog = []
for x in range(len(data)):
    pog.append(np.sqrt((((-8 * (np.pi ** 2) * plengths[x]) / (datamean[x] ** 3) * stats.sem(datamean)) ** 2) + \
        ((4 * (np.pi ** 2) / (datamean[x] ** 2) * 0.001) ** 2)))



plt.title("g against L")
plt.xlabel("Pendulum length (M)")
plt.ylabel("gravity ($ms^{-2}$)")
plt.errorbar(plengths, gvalues, xerr=None, yerr=pog, ls='None')
plt.scatter(plengths, gvalues, marker='.', label="data")
plt.legend()

print("mean gravity = {} +- {}".format(np.mean(gvalues), pog[4]))



