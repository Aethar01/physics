import math
import statistics as s
import numpy as np
from scipy import stats, optimize as opt, special
from matplotlib import pyplot as plt

def funcpog(x, a, b):
    return (a * x) + b

def func1(x, a, b):
    dog = []
    for i in range(len(x)):
        dog.append((x[i] * a) + b)
    return dog

def Exp(x, a, b):
    dog = []
    for i in range(len(x)):
        dog.append(a * np.exp(b * x[i]))
    return dog

def getData(filename):
    a, b = np.genfromtxt(filename, \
                                        unpack = True, \
                                        usecols = (0, 1), \
                                        comments = '#', \
                                        dtype = str)

    a1 = [eval(x) for x in a]
    b1 = [eval(x) for x in b]
    return a1, b1

def plot(x, y, optimized=None, xerr=None, yerr=None,  xname=None, yname=None, cursed=None):
    #if cursed==True:
    #    for i in range(len(plt.style.available)):
    #        plt.style.use(plt.style.available[-i])
    #else:
    #    plt.style.use('classic')
    plt.style.use('seaborn-whitegrid')
    plt.figure(dpi=1200)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.errorbar(x, y, yerr=yerr, xerr=xerr, ls='None', ecolor='#2f90a1')
    plt.plot(x, y, marker='.', ls='None', color='#2f90a1')
    plt.plot(x, func1(x, optimized[0], optimized[1]), '-', label="fit = $({} * x) + {}$".format(optimized[0].round(3), optimized[1].round(3)), color='#2fa14d')
    plt.legend()
    plt.show()

I1, V1 = getData("solar1.txt")
I2, V2 = getData("solar2.txt")
R3, I3 = getData("solar3.txt")


I1 = [x/1000 for x in I1]
I2 = [x/1000 for x in I2]
I3 = [x/1000 for x in I3]
pog=True
#R3 = [1/x for x in R3]
V3 = np.multiply(I3, R3)
sem1 = stats.sem(V1)
sem1 = [sem1] * len(V1)
sem2 = stats.sem(V2)
sem2 = [sem2] * len (V2)
sem3 = stats.sem(I1)
sem3 = [sem3] * len(I1)
sem4 = stats.sem(I2)
sem4 = [sem4] * len(I2)
sem5 = stats.sem(R3)
sem5 = [sem5] * len(R3)
sem6 = stats.sem(I3)
sem6 = [sem6] * len(I3)
sem7 = stats.sem(V3)
sem7 = [sem7] * len(V3)

print(V3)

optimized1, pcov = opt.curve_fit(func1, np.asarray(V1), np.asarray(I1), sigma=sem3, absolute_sigma=True)
optimized2, pcov = opt.curve_fit(func1, np.asarray(V2), np.asarray(I2), sigma=sem4, absolute_sigma=True)
optimized3, pcov = opt.curve_fit(func1, np.asarray(V3), np.asarray(I3), sigma=sem7, absolute_sigma=True)

plot(V1, I1, xerr=sem1, yerr=sem3, xname='$v[V](\\pm{}$)'.format(round(sem3[0], 3)), yname='$I[A](\\pm{}$)'.format(round(sem1[0], 3)), optimized=optimized1, cursed=True)
plot(V2, I2, xerr=sem2, yerr=sem4, xname='$v[V](\\pm{}$)'.format(round(sem4[0], 3)), yname='$I[A](\\pm{}$)'.format(round(sem2[0], 3)), optimized=optimized2, cursed=False)
plot(V3, I3, yerr=sem6, xerr=sem7, yname='${} [A] (\\pm{}$)'.format('{I}', round(sem6[0], 3)), xname='${} [V] (\\pm{}$)'.format('{v}', round(sem7[0], 3)), optimized=optimized3, cursed=False)




#u1 = [1/x * 100 for x in u]
#v1 = [1/x * 100 for x in v]
#pog=False
#plot(u1, v1, xname="$\\frac{1}{u} (m^{-1})$", yname="$\\frac{1}{v} (m^{-1})$")


 #if not pog:
     #    plt.plot(np.linspace(2.5, 3.75), [-1* x + 5 for x in np.linspace(2.5, 3.75)], label = '$fit = -1(\\pm0.05)x + 5(\\pm0.02)$')
     #    plt.legend()