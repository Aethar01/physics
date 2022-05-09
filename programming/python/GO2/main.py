import math
import statistics as s
import numpy as np
from scipy import stats, optimize as opt, special
from matplotlib import pyplot as plt


def getData(filename):
    a, b = np.genfromtxt(filename, \
                                        unpack = True, \
                                        usecols = (0, 1), \
                                        comments = '#', \
                                        dtype = str)

    a1 = [eval(x) for x in a]
    b1 = [eval(x) for x in b]
    return a1, b1

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
        plt.plot(np.linspace(2.5, 3.75), [-1.2* x + 5.65 for x in np.linspace(2.5, 3.75)], label = '$fit = -1.2(\\pm0.05)x + 5.65$')
        plt.legend()
    plt.show()

u, v = getData("lens.txt")

u1 = [1/x * 100 for x in u]
v1 = [1/x * 100 for x in v]
pog=False
plot(u1, v1, xname="$\\frac{1}{u} (m^{-1})$", yname="$\\frac{1}{v} (m^{-1})$")