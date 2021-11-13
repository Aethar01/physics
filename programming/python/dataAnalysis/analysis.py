'''pog'''
import random
import statistics as s
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

def getstats():

    Age, Heightin, Weightlbs = np.loadtxt('anthropometry.dat', \
                                        unpack = True, \
                                        usecols = (1, 2, 3), \
                                        delimiter = ',')

    # print(type(Heightin))
    Heightin = Heightin.tolist()
    # print(Heightin)

    anthro = open("anthroanalys.txt", "w")

    anthro.write("# sample number, mean, std, sem \n")

    for i in range(100):
        randheights = random.sample(Heightin, k=100)
        mean = s.mean(randheights)
        std = np.std(randheights)
        sem = stats.sem(randheights)
        anthro.write("{}, {}, {}, {} \n".format(i, mean, std, sem))

    anthro.close()

def analysestats():

    sample1, mean1, std1, sem1 = np.loadtxt(\
        'anthroanalys.txt', \
        unpack = True, \
        usecols = (0, 1, 2, 3), \
        delimiter = ',' \
    )

    plt.hist(sem1)
    plt.show()

def umeancalc():
    Heightin= np.loadtxt('anthropometry.dat', \
                                        unpack = True, \
                                        usecols = (2), \
                                        delimiter = ',')

    # print(type(Heightin))
    Heightin = Heightin.tolist()
    umean = s.mean(Heightin)
    return umean

def confinter():
    sample1, mean1, std1, sem1 = np.loadtxt(\
        'anthroanalys.txt', \
        unpack = True, \
        usecols = (0, 1, 2, 3), \
        delimiter = ',' \
    )

    umean = umeancalc()

    confinter = 0

    for i, j in zip(mean1, sem1):
        if umean >= (i - j) and umean <= (i + j):
            confinter += 1

    return("{} / 100".format(confinter))   
    
print(confinter())
print(confintertotal())