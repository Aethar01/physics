import math
import statistics as s
import numpy as np
from scipy import stats, optimize as opt, special
from matplotlib import pyplot as plt

def func1(x, a, b):
    x1 = np.array(x)
    a1 = np.array(b)
    b1 = np.array(b)
    y = x1*a1 + b1
    return y



def getData(filename):
    a, b, c = np.genfromtxt(filename, \
                                        unpack = True, \
                                        usecols = (0, 1, 2), \
                                        comments = '#', \
                                        dtype = str)

    a1 = [eval(x) for x in a]
    b1 = [eval(x) for x in b]
    c1 = [eval(x) for x in c]
    return a1, b1, c1

def plot(x, y, optimized=None, xerr=None, yerr=None,  xname=None, yname=None):
    plt.figure(dpi=1200)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.errorbar(x, y, xerr, yerr, ls='None')
    plt.plot(x, y, marker='x', ls='None')
    # if any(x == None for x in optimized):
    #     pass
    # else:
    #     
    #     plt.plot(x, func1(x, optimized[0], optimized[1]), '-', label="fit = $x*{}$ + {}".format(optimized[0].round(3), optimized[1].round(3)))
    if not pog:
        plt.plot(np.linspace(0, 0.65), [1.55* x for x in np.linspace(0, 0.65)], label = '$fit = 1.55(\\pm0.02)x$')
        plt.legend()
    plt.show()

i, c, r = getData('data1.txt')[0],getData('data1.txt')[1],getData('data1.txt')[2]
pog = True
plot(i, c, xerr=0.025, yerr=0.025, xname='$\\theta_i$', yname='$\\theta_c$')
pog = False
# optimized1, pcov1 = opt.curve_fit(func1, np.array([np.sin(np.pi/180*x) for x in i]), np.array([np.sin(np.pi/180*x) for x in r]))
# print(optimized1)

plot([np.sin(np.pi/180*x) for x in r], [np.sin(np.pi/180*x) for x in i], xerr=np.sin(np.pi/180*0.025), yerr=np.sin(np.pi/180*0.025), xname='$sin(\\theta_r)$', yname='$sin(\\theta_i)$')